# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(900, 0))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.913, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 180));\n"
"\n"
"")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 15, 0, 15)
        self.l_main = QLabel(self.frame_6)
        self.l_main.setObjectName(u"l_main")
        self.l_main.setMinimumSize(QSize(864, 200))
        self.l_main.setMaximumSize(QSize(864, 200))
        self.l_main.setLayoutDirection(Qt.LeftToRight)
        self.l_main.setStyleSheet(u"background-color: black;\n"
"border: 1px solid white;E")
        self.l_main.setScaledContents(True)
        self.l_main.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.l_main)


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(220, 230))
        self.frame_10.setMaximumSize(QSize(220, 230))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_10)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.frame_advanced_options = QFrame(self.frame_10)
        self.frame_advanced_options.setObjectName(u"frame_advanced_options")
        self.frame_advanced_options.setStyleSheet(u"")
        self.frame_advanced_options.setFrameShape(QFrame.StyledPanel)
        self.frame_advanced_options.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_advanced_options)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.frame_7 = QFrame(self.frame_advanced_options)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(150, 0))
        self.frame_7.setMaximumSize(QSize(150, 16777215))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.slider_anomaly_threshold = QSlider(self.frame_7)
        self.slider_anomaly_threshold.setObjectName(u"slider_anomaly_threshold")
        self.slider_anomaly_threshold.setMaximum(100)
        self.slider_anomaly_threshold.setValue(50)
        self.slider_anomaly_threshold.setOrientation(Qt.Horizontal)
        self.slider_anomaly_threshold.setTickPosition(QSlider.TicksBelow)
        self.slider_anomaly_threshold.setTickInterval(5)

        self.verticalLayout_6.addWidget(self.slider_anomaly_threshold)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_advanced_options)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(150, 0))
        self.frame_8.setMaximumSize(QSize(150, 16777215))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.slider_peak_threshold = QSlider(self.frame_8)
        self.slider_peak_threshold.setObjectName(u"slider_peak_threshold")
        self.slider_peak_threshold.setOrientation(Qt.Horizontal)
        self.slider_peak_threshold.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_3.addWidget(self.slider_peak_threshold)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame = QFrame(self.frame_advanced_options)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 0))
        self.frame.setMaximumSize(QSize(150, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.slider_window_length = QSlider(self.frame)
        self.slider_window_length.setObjectName(u"slider_window_length")
        self.slider_window_length.setOrientation(Qt.Horizontal)
        self.slider_window_length.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_7.addWidget(self.slider_window_length)


        self.verticalLayout_4.addWidget(self.frame)

        self.checkbox_analysis = QCheckBox(self.frame_advanced_options)
        self.checkbox_analysis.setObjectName(u"checkbox_analysis")
        self.checkbox_analysis.setMinimumSize(QSize(150, 0))
        self.checkbox_analysis.setMaximumSize(QSize(150, 16777215))
        self.checkbox_analysis.setLayoutDirection(Qt.LeftToRight)
        self.checkbox_analysis.setChecked(True)

        self.verticalLayout_4.addWidget(self.checkbox_analysis)


        self.verticalLayout_2.addWidget(self.frame_advanced_options)


        self.horizontalLayout_2.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.913, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 180));\n"
"")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.l_sub = QLabel(self.frame_9)
        self.l_sub.setObjectName(u"l_sub")
        self.l_sub.setMinimumSize(QSize(432, 100))
        self.l_sub.setMaximumSize(QSize(432, 100))
        self.l_sub.setStyleSheet(u"background-color: black;\n"
"border: 1px solid white;\n"
"")

        self.horizontalLayout_5.addWidget(self.l_sub)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(220, 230))
        self.frame_11.setMaximumSize(QSize(220, 230))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 9, -1, -1)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_style = QFrame(self.frame_12)
        self.frame_style.setObjectName(u"frame_style")
        self.frame_style.setFrameShape(QFrame.NoFrame)
        self.frame_style.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_style)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_style)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_10.addWidget(self.label_4)

        self.slider_fill_percentage = QSlider(self.frame_13)
        self.slider_fill_percentage.setObjectName(u"slider_fill_percentage")
        self.slider_fill_percentage.setOrientation(Qt.Horizontal)

        self.verticalLayout_10.addWidget(self.slider_fill_percentage)


        self.verticalLayout_9.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_style)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_11.addWidget(self.label_5)

        self.cb_analysis_color = QComboBox(self.frame_14)
        self.cb_analysis_color.setObjectName(u"cb_analysis_color")

        self.verticalLayout_11.addWidget(self.cb_analysis_color)


        self.verticalLayout_9.addWidget(self.frame_14)


        self.verticalLayout_8.addWidget(self.frame_style)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.bt_load = QPushButton(self.frame_11)
        self.bt_load.setObjectName(u"bt_load")
        self.bt_load.setMinimumSize(QSize(0, 0))
        self.bt_load.setMaximumSize(QSize(1000, 16777215))

        self.verticalLayout_5.addWidget(self.bt_load)

        self.bt_style_options = QPushButton(self.frame_11)
        self.bt_style_options.setObjectName(u"bt_style_options")
        self.bt_style_options.setCheckable(True)

        self.verticalLayout_5.addWidget(self.bt_style_options)

        self.bt_advanced_options = QPushButton(self.frame_11)
        self.bt_advanced_options.setObjectName(u"bt_advanced_options")
        self.bt_advanced_options.setCheckable(True)

        self.verticalLayout_5.addWidget(self.bt_advanced_options)


        self.horizontalLayout_2.addWidget(self.frame_11)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_stop = QPushButton(self.frame_3)
        self.bt_stop.setObjectName(u"bt_stop")

        self.horizontalLayout_3.addWidget(self.bt_stop)

        self.bt_start = QPushButton(self.frame_3)
        self.bt_start.setObjectName(u"bt_start")

        self.horizontalLayout_3.addWidget(self.bt_start)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 900, 21))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTheme = QMenu(self.menuBar)
        self.menuTheme.setObjectName(u"menuTheme")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTheme.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.l_main.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Anomaly Threshold", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Peak Height Threshold", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Search Window Length", None))
        self.checkbox_analysis.setText(QCoreApplication.translate("MainWindow", u"Analysis Mode", None))
        self.l_sub.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Difference Fill Percentage", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Analysis Color", None))
        self.bt_load.setText(QCoreApplication.translate("MainWindow", u"Load Signal", None))
        self.bt_style_options.setText(QCoreApplication.translate("MainWindow", u"Style Options", None))
        self.bt_advanced_options.setText(QCoreApplication.translate("MainWindow", u"Advanced Options", None))
        self.bt_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.bt_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

