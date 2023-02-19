# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'bright_variant.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
                               QPushButton, QSizePolicy, QSplitter, QStatusBar,
                               QTextEdit, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(951, 875)
        MainWindow.setStyleSheet(u"\n"
                                 "background-color: rgb(170, 170, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 230, 861, 32))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.input_label = QTextEdit(self.centralwidget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setGeometry(QRect(10, 270, 871, 81))
        self.input_label.setMaximumSize(QSize(16777215, 150))
        self.input_label.setFont(font)
        self.input_label.setLayoutDirection(Qt.LeftToRight)
        self.input_label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.check_button = QPushButton(self.centralwidget)
        self.check_button.setObjectName(u"check_button")
        self.check_button.setGeometry(QRect(290, 360, 301, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_button.sizePolicy().hasHeightForWidth())
        self.check_button.setSizePolicy(sizePolicy)
        self.check_button.setMaximumSize(QSize(16777215, 16777215))
        self.check_button.setFont(font)
        self.check_button.setStyleSheet(
            u"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
            "background-color: rgb(0, 255, 0);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 440, 141, 32))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 10, 788, 32))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 40, 801, 61))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.special_label = QComboBox(self.centralwidget)
        self.special_label.addItem("")
        self.special_label.setObjectName(u"special_label")
        self.special_label.setGeometry(QRect(250, 160, 441, 61))
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        self.special_label.setFont(font2)
        self.special_label.setLayoutDirection(Qt.LeftToRight)
        self.name_label = QTextEdit(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(220, 90, 501, 61))
        self.name_label.setMaximumSize(QSize(16777215, 150))
        self.name_label.setFont(font)
        self.name_label.setLayoutDirection(Qt.LeftToRight)
        self.name_label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.result_label = QTextEdit(self.centralwidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(50, 470, 791, 121))
        self.result_label.setMaximumSize(QSize(16777215, 150))
        self.result_label.setFont(font)
        self.result_label.setLayoutDirection(Qt.LeftToRight)
        self.result_label.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
                                        "")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(230, 690, 441, 91))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_6 = QLabel(self.splitter_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.label_6)
        self.station = QTextEdit(self.splitter_2)
        self.station.setObjectName(u"station")
        self.station.setMaximumSize(QSize(16777215, 150))
        self.station.setFont(font)
        self.station.setLayoutDirection(Qt.LeftToRight)
        self.station.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.splitter_2.addWidget(self.station)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(90, 790, 651, 81))
        self.splitter.setOrientation(Qt.Horizontal)
        self.add_button = QPushButton(self.splitter)
        self.add_button.setObjectName(u"add_button")
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        self.add_button.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(17)
        font3.setBold(True)
        self.add_button.setFont(font3)
        self.add_button.setStyleSheet(
            u"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
            "background-color: rgb(0, 255, 0);")
        self.splitter.addWidget(self.add_button)
        self.pushButton_2 = QPushButton(self.splitter)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(237, 51, 59);")
        self.splitter.addWidget(self.pushButton_2)
        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(70, 600, 741, 51))
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.working_label = QComboBox(self.splitter_3)
        self.working_label.addItem("")
        self.working_label.addItem("")
        self.working_label.setObjectName(u"working_label")
        self.working_label.setFont(font1)
        self.working_label.setLayoutDirection(Qt.LeftToRight)
        self.splitter_3.addWidget(self.working_label)
        self.region_label = QComboBox(self.splitter_3)
        self.region_label.addItem("")
        self.region_label.addItem("")
        self.region_label.addItem("")
        self.region_label.addItem("")
        self.region_label.setObjectName(u"region_label")
        self.region_label.setFont(font1)
        self.region_label.setLayoutDirection(Qt.LeftToRight)
        self.splitter_3.addWidget(self.region_label)
        self.taking_label = QComboBox(self.splitter_3)
        self.taking_label.addItem("")
        self.taking_label.addItem("")
        self.taking_label.setObjectName(u"taking_label")
        self.taking_label.setFont(font1)
        self.taking_label.setLayoutDirection(Qt.LeftToRight)
        self.splitter_3.addWidget(self.taking_label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.special_label.setCurrentIndex(0)
        self.working_label.setCurrentIndex(0)
        self.region_label.setCurrentIndex(0)
        self.taking_label.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u041e\u043a\u043d\u043e \u0434\u043b\u044f \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u043d\u0438\u044f",
                                                             None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u041f\u043e\u043c\u0435\u0441\u0442\u0438\u0442\u0435 \u043a\u0443\u0440\u0441\u043e\u0440 \u0432 \u043d\u0438\u0436\u043d\u0435\u0435 \u043f\u043e\u043b\u0435 \u0438 \u043d\u0430\u0447\u0438\u043d\u0430\u0439\u0442\u0435 \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435",
                                                      None))
        self.check_button.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c",
                                       None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0437 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435",
                                                        None))
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0415\u0441\u043b\u0438 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0430 \u043d\u0435\u0442, \u0442\u043e \u0432\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \"\u0434\u0440\u0443\u0433\u043e\u0435\"",
                                                        None))
        self.special_label.setItemText(0,
                                       QCoreApplication.translate("MainWindow", u"\u0434\u0440\u0443\u0433\u043e\u0435",
                                                                  None))

        self.name_label.setHtml(QCoreApplication.translate("MainWindow",
                                                           u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:'Ubuntu'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
                                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u0430\u0448\u0435 \u0438\u043c\u044f</p></body></html>",
                                                           None))
        self.result_label.setHtml(QCoreApplication.translate("MainWindow",
                                                             u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                             "p, li { white-space: pre-wrap; }\n"
                                                             "</style></head><body style=\" font-family:'Ubuntu'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
                                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                             None))
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u043d\u0446\u0438\u044f:", None))
        self.station.setHtml(QCoreApplication.translate("MainWindow",
                                                        u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:'Ubuntu'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
                                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                        None))
        self.add_button.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443",
                                                           None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.working_label.setItemText(0, QCoreApplication.translate("MainWindow",
                                                                     u"\u0418\u0441\u043f\u0440\u0430\u0432\u043d\u043e",
                                                                     None))
        self.working_label.setItemText(1, QCoreApplication.translate("MainWindow",
                                                                     u"\u041d\u0435 \u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e",
                                                                     None))

        self.region_label.setItemText(0, QCoreApplication.translate("MainWindow", u"1 \u0426\u0435\u043d\u0442\u0440",
                                                                    None))
        self.region_label.setItemText(1, QCoreApplication.translate("MainWindow", u"2 \u0421\u0412", None))
        self.region_label.setItemText(2, QCoreApplication.translate("MainWindow", u"3 \u042e\u0412", None))
        self.region_label.setItemText(3, QCoreApplication.translate("MainWindow", u"5 \u0421\u0417", None))

        self.taking_label.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0430\u044e", None))
        self.taking_label.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0440\u0443", None))

    # retranslateUi


class GUI_controller(QMainWindow):
    def __init__(self, parent=None):
        super(GUI_controller, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.name_label.toPlainText()
        print(self.ui.special_label.currentText())
        self.ui.input_label.toPlainText()
        self.ui.check_button.clicked.connect(self.analyzer)
        self.ui.result_label.toPlainText()
        self.ui.working_label.currentText()
        self.ui.region_label.currentText()
        self.ui.taking_label.currentText()
        self.ui.station.toPlainText()
        self.ui.add_button.clicked.connect(self.add_to_table)
        self.ui.pushButton_2.clicked.connect(self.delete)

    def analyzer(self):
        pass

    def delete(self):
        pass

    def add_to_table(self):
        pass


if __name__ == '__main__':
    app = QApplication()
    window = GUI_controller()
    window.show()
    sys.exit(app.exec())