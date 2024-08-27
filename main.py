from UI.UserInterface import UserInterface, QApplication, QByteArray, np, QImage





if __name__ == "__main__":
    app = QApplication([])
    window = UserInterface()
    window.show()
    app.exec()