import numpy as np
import cv2
from scipy.signal import find_peaks
from datetime import datetime
import threading
from typing import Tuple, List

from assets.transformation_functions import SignalTransformer
from assets.UserSettings import UserSettings
from assets.settings import *
from assets.utils import map_to_rgb
from models.AnomalyDetector import AnomalyDetector

MODEL_DEFAULT = AnomalyDetector("models/final_model.keras")




class SignalHandler:

    def __init__(self, signal: np.ndarray, transformer: SignalTransformer, lock: threading.Lock, model: AnomalyDetector = MODEL_DEFAULT):
        self.user_settings = UserSettings()
        self.signal = signal # original full loaded signal
        self.transformer = transformer # function to transform signal
        self.model = model # model for anomaly detection
        self.lock = lock # lock for threading

        self.run_signal = True # flag for stopping the signal view

        self.frame_main = np.ones((HEIGHT, WIDTH, 3), dtype=np.uint8) * 0 # frame for main signal view
        self.signal_view = self.transformer._normalize_signal(self.signal) # signal to be viewed on main frame
        self.sub_signal_frame = None # frame for sub signal view

        self.window_length = FRAME_SIZE // 2 # length of window to be analyzed in terms of peaks
        self.ii = 0 # index for window analysis

        self.__warm_up_model()


    
    def update_signal_frame(self, idx: int) -> np.ndarray:
            if idx < len(self.signal_view):
                with self.lock:
                    self._draw_next_signal_frame(idx)

                # drawing rectangles in the analysis area, finding peaks and drawing them
                if (idx > self.window_length and idx % self.window_length == 0) or (idx == self.window_length): # 
                    if self._get_analyze_state():
                        self._draw_peak_search_area()

                    self.find_signal_peaks()
                    self.ii += 1
            
                self.run_signal = True # True - continue the signal
            else:
                self.run_signal = False # False - end of the signal
            
            

    def find_signal_peaks(self) -> None:
        # transforming only the analysis window
        signal_window = self.transformer.transform_signal(self.signal[self.ii*self.window_length:(self.ii+1)*self.window_length])
        threshold = self.user_settings.peak_finding_threshold
        max_peaks = self.user_settings.max_peaks
        peaks = self._get_n_highest_peaks(signal_window, max_peaks, threshold, 10)

        if self._get_analyze_state():
            self._draw_found_peaks(peaks)

        self.make_predictions(peaks)
        

    
    def make_predictions(self, peaks: np.ndarray) -> np.ndarray:
        if len(peaks) > 0:
            start_time = datetime.now()
            peaks_results = []

            for p in peaks:
                peak_idx = self.ii * self.window_length + int(self.window_length / FRAME_SIZE * p) # index of the peak in the full signal

                if peak_idx > FRAME_SIZE // 2: # the half
                    prediction_window = self.transformer.transform_signal(np.hstack([self.signal[peak_idx-432:peak_idx], self.signal[peak_idx:peak_idx+432]]))
                    csf = np.ones((200, FRAME_SIZE, 3), dtype=np.uint8) * 0 # frame for sub signal view
                    prediction = self.predict_anomaly(prediction_window)

                    color = map_to_rgb(prediction[1][0])
                    peaks_results.append((p, color))

                    self._draw_sub_frame(csf, prediction_window, prediction[0][0], color) # drawing the sub window

                    self.sub_signal_frame = cv2.resize(csf, SUB_WINDOW_SHAPE, interpolation=cv2.INTER_LINEAR)
            

            end_time = datetime.now()
            delay = (end_time-start_time).microseconds / 1000 / 3
            
            with self.lock:
                self._draw_annotations(peaks_results, delay)

    

    def predict_anomaly(self, signal: np.ndarray) -> float:
        return self.model.predict(signal, self.user_settings.anomaly_threshold)
    


    def get_signal_frame(self) -> np.ndarray:
        return self.frame_main
    


    def toggle_analysis(self):
        self.user_settings.set_analyze_mode(not self._get_analyze_state())



    def set_model_threshold(self, threshold: float) -> None:
        try:
            self.user_settings.set_anomaly_threshold(threshold)
        except ValueError:
            pass

    
    def set_peak_finding_threshold(self, threshold: float) -> None:
        try:    
            self.user_settings.set_peak_finding_threshold(threshold)
        except ValueError:
            pass
    

    def set_sub_frame_fill_percentage(self, percentage: int) -> None:
        try:    
            self.user_settings.set_sub_frame_fill_percentage(percentage)
        except ValueError:
            pass
    

    def set_analyze_mode_color(self, color: Tuple[int, int, int]) -> None:
        try:    
            self.user_settings.set_analyze_mode_color(color)
        except ValueError:
            pass

    
    def set_max_peaks(self, value: int) -> None:
        try:
            self.user_settings.set_max_peaks(value)
        except ValueError:
            pass







    def _draw_next_signal_frame(self, idx: int) -> None:
        self.frame_main[:, :-int(SCALE_X)] = self.frame_main[:, int(SCALE_X):]  # sliding window
        self.frame_main[:, -int(SCALE_X):] = 0 # filling new space with black

        y1 = int(SCALE_Y - self.signal_view[idx-1] * SCALE_Y) # drawing the signal
        y2 = int(SCALE_Y - self.signal_view[idx] * SCALE_Y)
        cv2.line(self.frame_main, (WIDTH - 1, y1), (WIDTH - 1, y2), (11, 212, 11), 1)

    

    def _draw_peak_search_area(self, h_bound: Tuple[int, int] = (50, 350)) -> None:
        x1_r = WIDTH - self.window_length
        x2_r = WIDTH - 1
        color = self.user_settings.analyze_mode_color

        cv2.rectangle(self.frame_main, (x1_r, h_bound[0]), (x2_r, h_bound[1]), color, 1)

    

    def _draw_found_peaks(self, peaks: np.ndarray) -> None:
        color = self.user_settings.analyze_mode_color
        for p in peaks:
            cv2.circle(self.frame_main, (WIDTH - self.window_length + int(self.window_length / 864 * p), 100), radius=2, color=color, thickness=3)

    

    def _draw_sub_frame(self, pixmap: np.ndarray, signal_window: np.ndarray, predicted_signal: np.ndarray, color: Tuple[int, int, int] = (0, 0, 255)) -> None:
        h, w = pixmap.shape[:2]
        for i in range(1, w): # drawing the sub window
            cv2.line(pixmap, (i-1, int(h - h*signal_window[i-1])), (i, int(h - h*signal_window[i])), color, 2)

        if self._get_analyze_state():
            self._draw_sub_frame_analysis(pixmap, signal_window, predicted_signal, color)


    
    def _draw_sub_frame_analysis(self, pixmap: np.ndarray, signal_window: np.ndarray, predicted_signal: np.ndarray, color: Tuple[int, int, int] = (255, 255, 255)) -> None: 
        h, w = pixmap.shape[:2]
        for i in range(1, w): # drawing the prediction
            cv2.line(pixmap, (i-1, int(200 - 200*predicted_signal[i-1])), (i, int(h - h*predicted_signal[i])), color, 2)
            if self.user_settings.sub_frame_fill_percentage == 0:
                modulo_val = w
            elif self.user_settings.sub_frame_fill_percentage == 100:
                modulo_val = 1
            else:
                modulo_val = 2
            if i % modulo_val == 0:
                cv2.line(pixmap, (i, int(200 - 200*predicted_signal[i-1])), (i, int(h - h*signal_window[i])), color, 1)

    

    def _draw_annotations(self, peaks_map: List[Tuple[int, Tuple[int, int, int]]], delay: float) -> None:
        for p, c in peaks_map: # drawing every peak, taking into account the relative window position on the main frame
            x_mid = (WIDTH-self.window_length-int(delay)) + int(self.window_length / 864 * p)
            cv2.circle(self.frame_main, (x_mid, 100), radius=4, color=c, thickness=3)
            cv2.line(self.frame_main, (x_mid-25, 10), (x_mid+25, 10), c, 2)


    def _get_analyze_state(self):
        return self.user_settings.analyze_mode
    


    def _get_n_highest_peaks(self, signal, n: int, height: float, distance: int) -> np.ndarray:
        res = find_peaks(signal, height=height, distance=distance)
        n_highest = np.argsort(res[1]["peak_heights"])[-n:]
        return res[0][n_highest]
    

    def __warm_up_model(self):
        self.model.predict(np.zeros((FRAME_SIZE,)), 0.5)
        self.model.predict(np.ones((FRAME_SIZE,)), 0.5)
    
    
    