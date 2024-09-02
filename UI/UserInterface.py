from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QByteArray, QTimer, Qt, QRunnable, Slot, QThreadPool
from UI.templates.MainWindow import Ui_MainWindow

from concurrent.futures import ThreadPoolExecutor
from threading import Lock

from assets.utils import *
from assets.transformation_functions import SignalTransformer
from assets.settings import *
from assets.SignalHandler import SignalHandler

import numpy as np
import cv2


window_size = 2*864
height, width = 400, 2*864
scale_x = width / window_size
scale_y = height

signal_test = load_full_ecg("data/arrythmia_rates/", "119")[0]

transformer = SignalTransformer()

frame = np.ones((height, width, 3), dtype=np.uint8) * 0
signal_tt = transformer._normalize_signal(signal_test)

LOCK = Lock()




class UserInterface(QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_TEST)
        self.lock = Lock()
        self.signal_handler = SignalHandler(signal_test, transformer, self.lock) # change to none and load signal later
        self.transformer = SignalTransformer()
        self.thread_pool = QThreadPool()
        self.frame_main = np.ones((HEIGHT, WIDTH, 3), dtype=np.uint8) * 0

        self.idx = 1

        # delete later - load_signal

        self.signal = load_full_ecg("data/arrythmia_rates/", "111")[0]
        self.signal_view = self.transformer._normalize_signal(self.signal)


        self.bt_start.clicked.connect(self.start_signal)
        self.bt_stop.clicked.connect(self.stop_signal)

        self.checkbox_analysis.setChecked(self.signal_handler._get_analyze_state())

        
        

        self.checkbox_analysis.clicked.connect(self.toggle_analysis)
        self.frame_advanced_options.hide()
        self.frame_style.hide()
        self.bt_advanced_options.clicked.connect(self.toggle_advanced_options)
        self.bt_style_options.clicked.connect(self.toggle_style_options)

        self.__initialize_slider_anomaly_threshold()
        self.__initialize_slider_fill_percentage()
        self.__initialize_slider_peak_threshold()
        self.__initialize_slider_window_length()

        self.cb_analysis_color.addItems([*COLORS.keys()])
        self.cb_analysis_color.currentIndexChanged.connect(self.update_analysis_color)
    
        

    
    def update_main_image(self, image: np.ndarray) -> None:
        image_resized = cv2.resize(image, (self.l_main.width(), self.l_main.height()), interpolation=cv2.INTER_LINEAR)
        qimage = QImage(image_resized.data, self.l_main.width(), self.l_main.height(), 3 * self.l_main.width(), QImage.Format_RGB888)
        self.l_main.setPixmap(QPixmap.fromImage(qimage))

    
    def update_sub_image(self, image: np.ndarray) -> None:
        qimage = QImage(image.data, self.l_sub.width(), self.l_sub.height(), 3 * self.l_sub.width(), QImage.Format_RGB888)
        self.l_sub.setPixmap(QPixmap.fromImage(qimage))





    def load_signal(self, signal_path: str, idx: str):
        self.signal = load_full_ecg(signal_path, idx)[0]

        signal_test = load_full_ecg("data/arrythmia_rates/", "111")[0]

        self.signal_view = self.transformer._normalize_signal(signal_test)


    def start_signal(self):
        self.timer.start(3)

    def stop_signal(self):
        self.timer.stop()





    def update_TEST(self):

        #self.signal_handler.update_signal_frame(self.idx)
        self.start_computation()
        with self.lock:
            self.update_main_image(self.signal_handler.get_signal_frame())


        if not self.check_signal_status():
            self.timer.stop()
        
        if self.signal_handler.sub_signal_frame is not None:
            self.update_sub_image(self.signal_handler.sub_signal_frame)
        self.idx += 1


    def check_signal_status(self) -> bool:
        return self.signal_handler.run_signal
    

    def start_computation(self):
        worker = ComputeNextFrame(self.signal_handler, self.idx)
        self.thread_pool.start(worker)

    
    def toggle_analysis(self):
        self.signal_handler.toggle_analysis()


    def toggle_advanced_options(self):
        if self.frame_advanced_options.isHidden():
            self.frame_advanced_options.show()
        else:
            self.frame_advanced_options.hide()


    def toggle_style_options(self):
        if self.frame_style.isHidden():
            self.frame_style.show()
        else:
            self.frame_style.hide()


    def update_anomaly_threshold(self, value: float):
        new_threshold = DEFAULT_THRESHOLD * (100 + value) / 100
        self.signal_handler.set_model_threshold(new_threshold)


    def update_fill_percentage(self, value: int):
        new_value = self.__cut_the_value(50, value)
        self.slider_fill_percentage.setValue(new_value)
        self.signal_handler.set_sub_frame_fill_percentage(new_value)

    
    def update_analysis_color(self, *args):
        color = COLORS[self.cb_analysis_color.currentText()]
        self.signal_handler.set_analyze_mode_color(color)

    
    def update_peak_threshold(self, value: float):
        new_threshold = self.__cut_the_value(5, value)
        self.slider_peak_threshold.setValue(new_threshold)
        self.signal_handler.set_peak_finding_threshold(new_threshold)

    
    def update_window_length(self, value: int):
        new_length = self.__cut_the_value(FRAME_SIZE // 4, value)
        self.slider_window_length.setValue(new_length)
        self.signal_handler.set_analyze_window_length(new_length)



    def __initialize_slider_fill_percentage(self):
        self.slider_fill_percentage.setSingleStep(50)
        self.slider_fill_percentage.setMinimum(0)
        self.slider_fill_percentage.setMaximum(100)
        self.slider_fill_percentage.setValue(100)
        self.slider_fill_percentage.valueChanged.connect(self.update_fill_percentage)

    
    def __initialize_slider_anomaly_threshold(self):
        self.slider_anomaly_threshold.setSingleStep(1)
        self.slider_anomaly_threshold.setMinimum(-10)
        self.slider_anomaly_threshold.setMaximum(10)
        self.slider_anomaly_threshold.setValue(0)
        self.slider_anomaly_threshold.valueChanged.connect(self.update_anomaly_threshold)


    def __initialize_slider_peak_threshold(self):
        self.slider_peak_threshold.setSingleStep(5)
        self.slider_peak_threshold.setMinimum(60)
        self.slider_peak_threshold.setMaximum(95)
        self.slider_peak_threshold.setValue(80)
        self.slider_peak_threshold.valueChanged.connect(self.update_peak_threshold)

    
    def __initialize_slider_window_length(self):
        self.slider_window_length.setSingleStep(FRAME_SIZE // 4)
        self.slider_window_length.setMinimum(FRAME_SIZE // 4)
        self.slider_window_length.setMaximum(FRAME_SIZE)
        self.slider_window_length.setValue(FRAME_SIZE // 2)
        self.slider_window_length.valueChanged.connect(self.update_window_length)

    
    def __cut_the_value(self, step: int, value: int) -> int:
        if value % step <= step // 2:
            return value - value % step
        else:
            return value + step - value % step


    


    






class ComputeNextFrame(QRunnable):
    def __init__(self, c_object: SignalHandler, idx: int):
        super().__init__()
        self.engine = c_object
        self.idx = idx

    @Slot()
    def run(self):
        self.engine.update_signal_frame(self.idx)