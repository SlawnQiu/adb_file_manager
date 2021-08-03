# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rename.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RenameWindow(object):
    def setupUi(self, RenameWindow):
        RenameWindow.setObjectName("RenameWindow")
        RenameWindow.resize(390, 160)
        RenameWindow.setMinimumSize(QtCore.QSize(390, 160))
        RenameWindow.setMaximumSize(QtCore.QSize(390, 160))
        self.centralwidget = QtWidgets.QWidget(RenameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setGeometry(QtCore.QRect(72, 89, 271, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.name_edit.setFont(font)
        self.name_edit.setObjectName("name_edit")
        self.ok_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ok_btn.setGeometry(QtCore.QRect(151, 124, 75, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ok_btn.setFont(font)
        self.ok_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image: url(:/logo/Resources/ad-solid.svg);\n"
"font: 9pt \"微软雅黑\";")
        self.ok_btn.setObjectName("ok_btn")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(-10, -10, 721, 461))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(5, 15, 31, 31))
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn.setStyleSheet("border-image: url(:/logo/Resources/arrow_back-24px.svg);")
        self.back_btn.setText("")
        self.back_btn.setIconSize(QtCore.QSize(30, 30))
        self.back_btn.setObjectName("back_btn")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(0, 54, 751, 21))
        self.label_16.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.181818 rgba(255, 255, 255, 0));")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 711, 55))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textBrowser_2.setAutoFillBackground(False)
        self.textBrowser_2.setStyleSheet("background-color: rgb(0, 121, 107);\n"
"font: 9pt \"微软雅黑\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(42, 84, 21, 31))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 109, 391, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(71, 71, 111, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(330, 90, 721, 81))
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(50, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -40, 401, 101))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.textBrowser_4.raise_()
        self.name_edit.raise_()
        self.ok_btn.raise_()
        self.label_16.raise_()
        self.textBrowser_2.raise_()
        self.label.raise_()
        self.line.raise_()
        self.label_2.raise_()
        self.label_23.raise_()
        self.label_12.raise_()
        self.label_3.raise_()
        self.back_btn.raise_()
        RenameWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RenameWindow)
        QtCore.QMetaObject.connectSlotsByName(RenameWindow)

    def retranslateUi(self, RenameWindow):
        _translate = QtCore.QCoreApplication.translate
        RenameWindow.setWindowTitle(_translate("RenameWindow", "重命名"))
        self.ok_btn.setText(_translate("RenameWindow", "确定"))
        self.textBrowser_4.setWhatsThis(_translate("RenameWindow", "背景"))
        self.textBrowser_2.setHtml(_translate("RenameWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("RenameWindow", "<html><head/><body><p><img src=\":/file_manager/Resources/file_manager/archive.svg\"/></p></body></html>"))
        self.label_2.setText(_translate("RenameWindow", "<html><head/><body><p><span style=\" color:#595959;\">修改文件名</span></p></body></html>"))
        self.label_12.setText(_translate("RenameWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">重命名</span></p></body></html>"))
