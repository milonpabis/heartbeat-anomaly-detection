from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap, QImage, QIcon
from PySide6.QtCore import QTimer, QRunnable, Slot, QThreadPool
from UI.templates.MainWindow import Ui_MainWindow

from threading import Lock

from assets.utils import *
from assets.transformation_functions import SignalTransformer
from assets.settings import *
from assets.SignalHandler import SignalHandler

import numpy as np
import cv2



class UserInterface(QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("UI/other/icon.png"))
        self.setWindowTitle("ECG Anomaly Detection")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.loop_handler)
        self.lock = Lock()
        self.signal_handler = None
        self.transformer = SignalTransformer()
        self.thread_pool = QThreadPool()
        self.frame_main = np.ones((HEIGHT, WIDTH, 3), dtype=np.uint8) * 0

        self.idx = 1 # frame number

        self._initialize_items()



    def loop_handler(self) -> None:
        """
        Main loop handler for updating the signal frames.
        Iterates the signal frames and updates the main and sub images.
        Stops the timer if the signal is finished.
        """
        self.start_computation()
        with self.lock:
            self.update_main_image(self.signal_handler.get_signal_frame())

        if not self.__check_signal_status():
            self.timer.stop()
        
        if self.signal_handler.sub_signal_frame is not None:
            self.update_sub_image(self.signal_handler.sub_signal_frame)
        self.idx += 1



    def load_signal(self) -> None:
        """
        Loads the signal from the file.
        """
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("ECG files (*.hea)")
        dialog.exec()
        if dialog.selectedFiles():
            try:
                file_name = dialog.selectedFiles()[0].split(".")[0]
                signal = load_signal_ecg(file_name)
                self.signal_handler = SignalHandler(signal, self.transformer, self.lock)
                self.idx = 1

                self.bt_start.setEnabled(True)
            except Exception as e:
                print(e)

    

    def start_computation(self) -> None:
        """
        Creates and starts a worker for the next frame computation.
        """
        worker = ComputeNextFrame(self.signal_handler, self.idx)
        self.thread_pool.start(worker)

    

    def update_main_image(self, image: np.ndarray) -> None:
        """
        Sets the given image in np.array format to the main frame.
        """
        image_resized = cv2.resize(image, (self.l_main.width(), self.l_main.height()), interpolation=cv2.INTER_LINEAR)
        qimage = QImage(image_resized.data, self.l_main.width(), self.l_main.height(), 3 * self.l_main.width(), QImage.Format_RGB888)
        self.l_main.setPixmap(QPixmap.fromImage(qimage))

    

    def update_sub_image(self, image: np.ndarray) -> None:
        """
        Sets the given image in np.array format to the sub frame.
        """
        qimage = QImage(image.data, self.l_sub.width(), self.l_sub.height(), 3 * self.l_sub.width(), QImage.Format_RGB888)
        self.l_sub.setPixmap(QPixmap.fromImage(qimage))



    def start_signal(self) -> None:
        self.timer.start(3) # 3 ms interval (should be 2.77 ms for 360 Hz and 864 length signal)



    def stop_signal(self) -> None:
        self.timer.stop()



    def toggle_analysis(self) -> None:
        """
        Turns on/off the analysis mode.
        """
        self.signal_handler.toggle_analysis()



    def toggle_advanced_options(self) -> None:
        """
        Hides/Shows the advanced options frame.
        """
        if self.frame_advanced_options.isHidden():
            self.frame_advanced_options.show()
        else:
            self.frame_advanced_options.hide()



    def toggle_style_options(self) -> None:
        """
        Hides/Shows the style options frame.
        """
        if self.frame_style.isHidden():
            self.frame_style.show()
        else:
            self.frame_style.hide()



    def update_anomaly_threshold(self, value: float) -> None:
        """
        Updates the anomaly detection model threshold.
        """
        new_threshold = DEFAULT_THRESHOLD * (100 + value) / 100
        self.signal_handler.set_model_threshold(new_threshold)



    def update_fill_percentage(self, value: int) -> None:
        """
        Updates the fill percentage of the sub frame.
        Uses 3 steps: No fill, 50% fill, 100% fill.
        """
        new_value = self.__cut_the_value(50, value)
        self.slider_fill_percentage.setValue(new_value)
        self.signal_handler.set_sub_frame_fill_percentage(new_value)

    

    def update_analysis_color(self, *args) -> None:
        """
        Updates the color of the analysis mode.
        """
        color = COLORS[self.cb_analysis_color.currentText()]
        self.signal_handler.set_analyze_mode_color(color)

    

    def update_peak_threshold(self, value: float) -> None:
        """
        Updates the peak threshold value.
        """
        new_threshold = self.__cut_the_value(5, value)
        self.slider_peak_threshold.setValue(new_threshold)
        self.signal_handler.set_peak_finding_threshold(new_threshold/100)

    
    def update_max_peaks(self, value: int) -> None:
        """
        Updates the maximum number of peaks to be found.
        """
        self.signal_handler.set_max_peaks(value)



    def _initialize_items(self) -> None:
        """
        Initializes the items in the UI.
        """
        # sliders
        self.__initialize_slider_anomaly_threshold()
        self.__initialize_slider_fill_percentage()
        self.__initialize_slider_peak_threshold()
        self.__initialize_slider_max_peaks()
        # combobox
        self.__initialize_combobox_analysis_color()
        # buttons signals
        self.bt_start.clicked.connect(self.start_signal)
        self.bt_stop.clicked.connect(self.stop_signal)
        self.bt_load.clicked.connect(self.load_signal)
        self.bt_advanced_options.clicked.connect(self.toggle_advanced_options)
        self.bt_style_options.clicked.connect(self.toggle_style_options)
        self.checkbox_analysis.clicked.connect(self.toggle_analysis)
        self.checkbox_analysis.setChecked(False)
        # others
        self.frame_advanced_options.hide()
        self.frame_style.hide()
        self.bt_start.setEnabled(False)



    def __initialize_slider_fill_percentage(self) -> None:
        self.slider_fill_percentage.setSingleStep(50)
        self.slider_fill_percentage.setMinimum(0)
        self.slider_fill_percentage.setMaximum(100)
        self.slider_fill_percentage.setValue(100)
        self.slider_fill_percentage.valueChanged.connect(self.update_fill_percentage)


    
    def __initialize_slider_anomaly_threshold(self) -> None:
        self.slider_anomaly_threshold.setSingleStep(1)
        self.slider_anomaly_threshold.setMinimum(-10)
        self.slider_anomaly_threshold.setMaximum(10)
        self.slider_anomaly_threshold.setValue(0)
        self.slider_anomaly_threshold.valueChanged.connect(self.update_anomaly_threshold)



    def __initialize_slider_peak_threshold(self) -> None:
        self.slider_peak_threshold.setSingleStep(5)
        self.slider_peak_threshold.setMinimum(60)
        self.slider_peak_threshold.setMaximum(95)
        self.slider_peak_threshold.setValue(80)
        self.slider_peak_threshold.valueChanged.connect(self.update_peak_threshold)


    def __initialize_slider_max_peaks(self) -> None:
        self.slider_max_peaks.setSingleStep(1)
        self.slider_max_peaks.setMinimum(1)
        self.slider_max_peaks.setMaximum(5)
        self.slider_max_peaks.setValue(2)
        self.slider_max_peaks.valueChanged.connect(self.update_max_peaks)


    
    def __initialize_combobox_analysis_color(self) -> None:
        self.cb_analysis_color.addItems([*COLORS.keys()])
        self.cb_analysis_color.setCurrentText("Blue")
        self.cb_analysis_color.currentIndexChanged.connect(self.update_analysis_color)

    

    def __check_signal_status(self) -> bool:
        return self.signal_handler.run_signal


    
    def __cut_the_value(self, step: int, value: int) -> int:
        """
        Cuts the value to the nearest multiple of the step.
        """
        if value % step <= step // 2:
            return value - value % step
        else:
            return value + step - value % step






class ComputeNextFrame(QRunnable):
    """
    Worker class for updating the signal frame.
    Uses QRunnable for multithreading.
    Simply runs the next frame computation in the signal handler.

    Parameters
    ----------
    c_object : SignalHandler
        The signal handler object.
    idx : int
        The index of the current frame.
    """
    def __init__(self, c_object: SignalHandler, idx: int):
        super().__init__()
        self.engine = c_object
        self.idx = idx


    @Slot()
    def run(self):
        self.engine.update_signal_frame(self.idx)