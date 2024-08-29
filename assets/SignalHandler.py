import numpy as np
import cv2
from scipy.signal import find_peaks

from assets.transformation_functions import SignalTransformer
from assets.settings import *



class SignalHandler:

    def __init__(self, signal: np.ndarray, transformer: SignalTransformer):
        self.signal = signal # original full loaded signal
        self.transformer = transformer # function to transform signal

        self.frame_main = np.ones((HEIGHT, WIDTH, 3), dtype=np.uint8) * 0 # frame for main signal view
        self.signal_view = self.transformer._normalize_signal(self.signal) # signal to be viewed on main frame
        self.sub_signal_frame = None # frame for sub signal view

        self.window_length = 432 # length of window to be analyzed in terms of peaks
        self.ii = 0 # index for window analysis


    
    def update_signal_frame(self, idx: int) -> np.ndarray:
        if idx < len(self.signal_view):

            self.frame_main[:, :-int(SCALE_X)] = self.frame_main[:, int(SCALE_X):]  # sliding window
            self.frame_main[:, -int(SCALE_X):] = 0 # filling new space with black

            y1 = int(SCALE_Y - self.signal_view[idx-1] * SCALE_Y) # drawing the signal
            y2 = int(SCALE_Y - self.signal_view[idx] * SCALE_Y)
            cv2.line(self.frame_main, (WIDTH - 1, y1), (WIDTH - 1, y2), (11, 212, 11), 1)

            # drawing rectangles in the analysis area, finding peaks and drawing them
            if (idx > self.window_length and idx % self.window_length == 0) or (idx == self.window_length): # 
                x1_r = WIDTH - self.window_length
                x2_r = WIDTH - 1
                cv2.rectangle(self.frame_main, (x1_r, 50), (x2_r, 350), (0, 0, 255), 1)
                self.find_signal_peaks()
                self.ii += 1


                # ------------------------------
                        
                # signal_window = transformer.transform_signal(signal[ii*window_length:(ii+1)*window_length])
                # peaks = find_peaks(signal_window, height=0.8)[0]
                        
                # if len(peaks) > 1 and abs(peaks[0] - peaks[1]) < 10:
                #     peaks = np.delete(peaks, 1)
                            
                # for p in peaks:
                #     cv2.circle(frame, ((800-window_length)+int(window_length/864*p), 100), radius=2, color=(0, 0, 255), thickness=3)
                #     peak_idx = ii*window_length+int(window_length/864*p)
                            
                #     if peak_idx > 432:
                #         prediction_window = transformer.transform_signal(np.hstack([signal[peak_idx-432:peak_idx], signal[peak_idx:peak_idx+432]]))
                #         csf = current_signal_frame.copy()
                #         #prediction = model.predict(prediction_window) #[2][0]
                #         #print(prediction[2][0], prediction[1])
                #         #color = map_to_rgb(prediction[1][0])
                #         color = (0, 255, 0)
                #         for oo in range(1, len(prediction_window)):
                #             cv2.line(csf, (oo-1, int(400 - 400*prediction_window[oo-1])), (oo, int(400 - 400*prediction_window[oo])), color, 1)
                                
                #         cv2.imshow("Current Signal Window", csf)
                        
                # ii += 1

        else:
            return False, self.frame_main # False - end of the signal

        return True, self.frame_main
    

    def find_signal_peaks(self):
        # transforming only the analysis window ( not needed if problems )
        signal_window = self.transformer.transform_signal(self.signal[self.ii*self.window_length:(self.ii+1)*self.window_length])
        peaks = find_peaks(signal_window, height=0.8)[0]
                        
        if len(peaks) > 1 and abs(peaks[0] - peaks[1]) < 10: # bugs were here so temporary solution
            peaks = np.delete(peaks, 1)
                            
        for p in peaks: # drawing every peak, taking into account the relative window position on the main frame
            cv2.circle(self.frame_main, ((WIDTH-self.window_length) + int(self.window_length / 864 * p), 100), radius=2, color=(0, 0, 255), thickness=3)

        self.update_sub_frame(peaks)


    
    def update_sub_frame(self, peaks: np.ndarray) -> np.ndarray:
        if len(peaks) > 0:

            for p in peaks:
                peak_idx = self.ii * self.window_length + int(self.window_length / 864 * p) # index of the peak in the full signal

                if peak_idx > 432: # the half
                    prediction_window = self.transformer.transform_signal(np.hstack([self.signal[peak_idx-432:peak_idx], self.signal[peak_idx:peak_idx+432]]))
                    csf = np.ones((200, 864, 3), dtype=np.uint8) * 0 # frame for sub signal view
                    #prediction = model.predict(prediction_window) #[2][0]
                    #print(prediction[2][0], prediction[1])
                    #color = map_to_rgb(prediction[1][0])
                    color = (0, 255, 0)
                    for oo in range(1, len(prediction_window)):
                        cv2.line(csf, (oo-1, int(200 - 200*prediction_window[oo-1])), (oo, int(200 - 200*prediction_window[oo])), color, 1)

                    self.sub_signal_frame = cv2.resize(csf, (432, 100), interpolation=cv2.INTER_LINEAR)
            