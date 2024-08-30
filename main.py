from UI.UserInterface import UserInterface, QApplication, QByteArray, np, QImage





if __name__ == "__main__":
    app = QApplication([])
    window = UserInterface()
    window.show()
    app.exec()




# TODO:

# - colorize the peaks on the main signal view
# - take care of the drawing anomalies caused by the delay in computation:
#   - separate drawing the pure signal from the analysis area
# - divide some functions in SignalHandler to make them more readable and separate