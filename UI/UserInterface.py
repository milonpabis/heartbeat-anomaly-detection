from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QByteArray, QTimer, Qt
from UI.templates.MainWindow import Ui_MainWindow

from assets.utils import load_full_ecg, convert_signal_to_image
from assets.transformation_functions import SignalTransformer
from assets.settings import *
from assets.SignalHandler import SignalHandler

import numpy as np
import cv2


window_size = 2*864
height, width = 400, 2*864
scale_x = width / window_size
scale_y = height

signal_test = load_full_ecg("data/arrythmia_rates/", "103")[0]

transformer = SignalTransformer()

frame = np.ones((height, width, 3), dtype=np.uint8) * 0  # 3 kanały dla BGR
signal_tt = transformer._normalize_signal(signal_test)






class UserInterface(QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.signal_handler = SignalHandler(signal_test, transformer) # change to none and load signal later
        self.transformer = SignalTransformer()
        self.frame_main = np.ones((HEIGHT, WIDTH, 3), dtype=np.uint8) * 0
        self.idx = 1

        # delete later - load_signal

        self.signal = load_full_ecg("data/arrythmia_rates/", "103")[0]
        self.signal_view = self.transformer._normalize_signal(self.signal)

        #self.signal = None
        #self.signal_view = None
        
        

        IMG_TEST = load_full_ecg("data/arrythmia_rates/", "100")
        IMG_TEST = convert_signal_to_image(IMG_TEST[0], IMG_TEST[1][5], self.l_sub.height(), self.l_sub.width())

        qimage = QImage(IMG_TEST.data, self.l_sub.width(), self.l_sub.height(), 3 * self.l_sub.width(), QImage.Format_RGB888)

        self.bt_start.clicked.connect(self.start_signal)
        self.pushButton.clicked.connect(self.stop_signal)

        self.l_sub.setPixmap(QPixmap.fromImage(qimage))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_TEST)
        

    
    def update_main_image(self, image: np.ndarray) -> None:
        qimage = QImage(image.data, self.l_main.width(), self.l_main.height(), 3 * self.l_main.width(), QImage.Format_RGB888)
        self.l_main.setPixmap(QPixmap.fromImage(qimage))

    
    def update_sub_image(self, image: np.ndarray) -> None:
        qimage = QImage(image.data, self.l_sub.width(), self.l_sub.height(), 3 * self.l_sub.width(), QImage.Format_RGB888)
        self.l_sub.setPixmap(QPixmap.fromImage(qimage))





    def load_signal(self, signal_path: str, idx: str):
        self.signal = load_full_ecg(signal_path, idx)[0]

        signal_test = load_full_ecg("data/arrythmia_rates/", "103")[0]

        self.signal_view = self.transformer._normalize_signal(signal_test)


    def start_signal(self):
        self.timer.start(3)

    def stop_signal(self):
        self.timer.stop()





    def update_TEST(self):

        gate, frame = self.signal_handler.update_signal_frame(self.idx)
        self.update_main_image(cv2.resize(frame, (self.l_main.width(), self.l_main.height()), interpolation=cv2.INTER_LINEAR))
        if not gate:
            self.timer.stop()
        
        if self.signal_handler.sub_signal_frame is not None:
            self.update_sub_image(self.signal_handler.sub_signal_frame)
        self.idx += 1




