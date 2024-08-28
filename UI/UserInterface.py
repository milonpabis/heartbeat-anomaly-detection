from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QByteArray, QTimer, Qt
from UI.templates.MainWindow import Ui_MainWindow

from assets.utils import load_full_ecg, convert_signal_to_image
from assets.transformation_functions import SignalTransformer

import numpy as np
import cv2

WIDTH = 864
HEIGHT = 400

COLORS = [Qt.white, Qt.black, Qt.red, Qt.green, Qt.blue, Qt.yellow, Qt.cyan, Qt.magenta, Qt.gray]

window_size = 2*864
height, width = 400, 2*864
scale_x = width / window_size
scale_y = height

signal_test = load_full_ecg("data/arrythmia_rates/", "100")[0]

transformer = SignalTransformer()

frame = np.ones((height, width, 3), dtype=np.uint8) * 0  # 3 kanały dla BGR
signal_tt = transformer._normalize_signal(signal_test)






class UserInterface(QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.idx = 1

        self.signal = None

        IMG_TEST = load_full_ecg("data/arrythmia_rates/", "100")
        IMG_TEST = convert_signal_to_image(IMG_TEST[0], IMG_TEST[1][5], self.l_sub.height(), self.l_sub.width())

        qimage = QImage(IMG_TEST.data, self.l_sub.width(), self.l_sub.height(), 3 * self.l_sub.width(), QImage.Format_RGB888)

        self.bt_start.clicked.connect(self.start_signal)
        self.pushButton.clicked.connect(self.stop_signal)

        self.l_sub.setPixmap(QPixmap.fromImage(qimage))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_TEST)
        

    
    def update_main_image(self, image: np.array):
        # pixmap = QPixmap(self.l_main.size())
        # pixmap.fill(COLORS[self.idx % len(COLORS)])
        # self.idx += 1
        
        # self.l_main.setPixmap(pixmap)

        qimage = QImage(image.data, self.l_main.width(), self.l_main.height(), 3 * self.l_main.width(), QImage.Format_RGB888)
        self.l_main.setPixmap(QPixmap.fromImage(qimage))


    def load_signal(self, signal_path: str, idx: str):
        self.signal = load_full_ecg(signal_path, idx)[0]


    def start_signal(self):
        self.timer.start(3)

    def stop_signal(self):
        self.timer.stop()





    def update_TEST(self):

        if self.idx < len(signal_tt):

            frame[:, :-int(scale_x)] = frame[:, int(scale_x):]
            frame[:, -int(scale_x):] = 0

            y1 = int(scale_y - signal_tt[self.idx-1] * scale_y)
            y2 = int(scale_y - signal_tt[self.idx] * scale_y)
            cv2.line(frame, (width - 1, y1), (width - 1, y2), (11, 212, 11), 1)
            #cv2.line(frame, (1, int(0.2*scale_y)), (width-1, int(0.2*scale_y)), (255, 255, 255), 1)

            self.update_main_image(cv2.resize(frame, (self.l_main.width(), self.l_main.height()), interpolation=cv2.INTER_LINEAR))
        else:
            self.timer.stop()
        
        self.idx += 1



            # window_length = 864 // 2


            # if (i > window_length and i % window_length == 0) or (i == window_length): # 
            #     x1_r = width - window_length
            #     x2_r = width - 1
            #     cv2.rectangle(frame, (x1_r, 50), (x2_r, 300), (0, 0, 255), 1)
                
            #     signal_window = transformer.transform_signal(signal[ii*window_length:(ii+1)*window_length])
            #     peaks = find_peaks(signal_window, height=0.8)[0]
                
            #     if len(peaks) > 1 and abs(peaks[0] - peaks[1]) < 10:
            #         peaks = np.delete(peaks, 1)
                    
            #     for p in peaks:
            #         cv2.circle(frame, ((800-window_length)+int(window_length/864*p), 100), radius=2, color=(0, 0, 255), thickness=3)
            #         peak_idx = ii*window_length+int(window_length/864*p)
                    
                    #if peak_idx > 432:
                        #prediction_window = transformer.transform_signal(np.hstack([signal[peak_idx-432:peak_idx], signal[peak_idx:peak_idx+432]]))
                        #csf = current_signal_frame.copy()
                        #prediction = model.predict(prediction_window) #[2][0]
                        #print(prediction[2][0], prediction[1])
                        #color = map_to_rgb(prediction[1][0])
                        #for oo in range(1, len(prediction_window)):
                        #    cv2.line(csf, (oo-1, int(400 - 400*prediction_window[oo-1])), (oo, int(400 - 400*prediction_window[oo])), color, 1)
                        
                        #cv2.imshow("Current Signal Window", csf)
                
                # ii += 1
