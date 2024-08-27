from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QByteArray
from UI.templates.MainWindow import Ui_MainWindow

import numpy as np

width, height = 100, 100
random_image_data = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)

qimage = QImage(random_image_data.data, width, height, 3 * width, QImage.Format_RGB888)

class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.bt_start.clicked.connect(lambda e: print('a'))

        self.l_main.setPixmap(QPixmap.fromImage(qimage))
