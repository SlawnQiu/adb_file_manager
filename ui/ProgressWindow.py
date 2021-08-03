# -*- coding: utf-8 -*-

# Form implementation generated from reading Ui file 'progress.Ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProgressWindow(object):
    def setupUi(self, ProgressWindow):
        ProgressWindow.setObjectName("ProgressWindow")
        ProgressWindow.resize(400, 120)
        ProgressWindow.setMinimumSize(QtCore.QSize(400, 120))
        ProgressWindow.setMaximumSize(QtCore.QSize(400, 120))
        self.centralwidget = QtWidgets.QWidget(ProgressWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(-100, -100, 721, 461))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(36, 79, 331, 23))
        self.progressBar.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 421, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setAutoFillBackground(False)
        self.textBrowser_2.setStyleSheet("background-color: rgb(0, 121, 107);\n"
"font: 9pt \"微软雅黑\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.condition = QtWidgets.QLabel(self.centralwidget)
        self.condition.setGeometry(QtCore.QRect(40, 50, 281, 21))
        self.condition.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.condition.setObjectName("condition")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -20, 491, 161))
        self.label.setText("")
        self.label.setObjectName("label")
        ProgressWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProgressWindow)
        QtCore.QMetaObject.connectSlotsByName(ProgressWindow)

    def retranslateUi(self, ProgressWindow):
        _translate = QtCore.QCoreApplication.translate
        self._translate = _translate
        ProgressWindow.setWindowTitle(_translate("ProgressWindow", "请稍后"))
        self.textBrowser_4.setWhatsThis(_translate("ProgressWindow", "背景"))
        self.textBrowser_2.setHtml(_translate("ProgressWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">请稍候 </span></p></body></html>"))
        self.condition.setText(_translate("ProgressWindow", "正在上传所选文件"))
