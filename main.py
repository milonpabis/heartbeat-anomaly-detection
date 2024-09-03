from UI.UserInterface import UserInterface, QApplication
import cProfile
import pstats

TESTS = 0


if __name__ == "__main__":
    if TESTS:
        profiler = cProfile.Profile()
        profiler.enable()
        ...
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


