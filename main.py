from UI.UserInterface import UserInterface, QApplication, QByteArray, np, QImage
from assets.SignalHandler import SignalHandler

from assets.transformation_functions import SignalTransformer
from threading import Lock
from models.AnomalyDetector import AnomalyDetector
from UI.UserInterface import signal_test

import cProfile
import pstats

TESTS = 0

def main():
    signal_handler = SignalHandler(signal_test, SignalTransformer(), Lock(), AnomalyDetector("models/final_model.keras"))
    signal_handler.update_signal_frame(0)


if __name__ == "__main__":
    if TESTS:
        profiler = cProfile.Profile()
        profiler.enable()
        main()
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats('cumtime')
        stats.print_stats()
    else:
        app = QApplication([])
        window = UserInterface()
        window.show()
        app.exec()







# TODO:

# - fix the rgb mapping function
# - implement the UserSettings class


