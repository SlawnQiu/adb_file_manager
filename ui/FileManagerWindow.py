# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filemanager.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileMangerWindow(object):
    def setupUi(self, FileMangerWindow):
        FileMangerWindow.setObjectName("FileMangerWindow")
        FileMangerWindow.resize(580, 530)
        FileMangerWindow.setMinimumSize(QtCore.QSize(580, 530))
        FileMangerWindow.setMaximumSize(QtCore.QSize(580, 530))
        FileMangerWindow.setSizeIncrement(QtCore.QSize(525, 410))
        FileMangerWindow.setBaseSize(QtCore.QSize(525, 410))
        self.centralwidget = QtWidgets.QWidget(FileMangerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FileList = QtWidgets.QListWidget(self.centralwidget)
        self.FileList.setGeometry(QtCore.QRect(20, 114, 301, 281))
        self.FileList.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FileList.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.FileList.setObjectName("FileList")
        self.path_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.path_edit.setGeometry(QtCore.QRect(100, 71, 331, 20))
        self.path_edit.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.path_edit.setObjectName("path_edit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 73, 16, 16))
        self.label.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.delFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delFile_btn.setGeometry(QtCore.QRect(460, 189, 81, 31))
        self.delFile_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delFile_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image: url(:/logo/Resources/ad-solid.svg);\n"
"font: 9pt \"微软雅黑\";")
        self.delFile_btn.setObjectName("delFile_btn")
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(460, 333, 81, 31))
        self.upload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upload.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image: url(:/logo/Resources/ad-solid.svg);\n"
"font: 9pt \"微软雅黑\";")
        self.upload.setObjectName("upload")
        self.copyFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.copyFile_btn.setGeometry(QtCore.QRect(360, 139, 81, 31))
        self.copyFile_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copyFile_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image: url(:/logo/Resources/ad-solid.svg);\n"
"font: 9pt \"微软雅黑\";")
        self.copyFile_btn.setObjectName("copyFile_btn")
        self.pasteFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pasteFile_btn.setGeometry(QtCore.QRect(360, 189, 81, 31))
        self.pasteFile_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pasteFile_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image: url(:/logo/Resources/ad-solid.svg);\n"
"font: 9pt \"微软雅黑\";")
        self.pasteFile_btn.setObjectName("pasteFile_btn")
        self.moveFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.moveFile_btn.setGeometry(QtCore.QRect(460, 139, 81, 31))
        self.moveFile_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.moveFile_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image: url(:/logo/Resources/ad-solid.svg);\n"
"font: 9pt \"微软雅黑\";")
        self.moveFile_btn.setObjectName("moveFile_btn")
        self.download_btn = QtWidgets.QPushButton(self.centralwidget)
        self.download_btn.setGeometry(QtCore.QRect(360, 333, 81, 31))
        self.download_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.download_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image: url(:/logo/Resources/ad-solid.svg);\n"
"font: 9pt \"微软雅黑\";")
        self.download_btn.setObjectName("download_btn")
        self.goto_btn = QtWidgets.QPushButton(self.centralwidget)
        self.goto_btn.setGeometry(QtCore.QRect(467, 70, 51, 21))
        self.goto_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.goto_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image: url(:/logo/Resources/ad-solid.svg);\n"
"font: 9pt \"微软雅黑\";")
        self.goto_btn.setObjectName("goto_btn")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 711, 55))
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
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(0, 54, 751, 21))
        self.label_16.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.181818 rgba(255, 255, 255, 0));")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(5, 15, 31, 31))
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn.setStyleSheet("border-image: url(:/logo/Resources/arrow_back-24px.svg);")
        self.back_btn.setText("")
        self.back_btn.setIconSize(QtCore.QSize(30, 30))
        self.back_btn.setObjectName("back_btn")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(-10, 36, 721, 521))
        self.textBrowser_4.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 66, 21, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(69, 57, 54, 12))
        self.label_3.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"color: rgb(100, 100, 100);")
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(342, 114, 221, 171))
        self.textEdit_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(342, 285, 221, 16))
        self.label_17.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.181818 rgba(255, 255, 255, 0));")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(563, 114, 16, 172))
        self.label_20.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.176136 rgba(255, 255, 255, 0));")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 54, 12))
        self.label_4.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"color: rgb(100, 100, 100);")
        self.label_4.setObjectName("label_4")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(320, 114, 16, 281))
        self.label_21.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.176136 rgba(255, 255, 255, 0));")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(20, 395, 302, 20))
        self.label_18.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.181818 rgba(255, 255, 255, 0));")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(340, 394, 221, 16))
        self.label_19.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.181818 rgba(255, 255, 255, 0));")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(561, 293, 16, 102))
        self.label_22.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.176136 rgba(255, 255, 255, 0));")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(340, 293, 221, 101))
        self.textEdit_3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.home_btn = QtWidgets.QPushButton(self.centralwidget)
        self.home_btn.setGeometry(QtCore.QRect(440, 70, 21, 21))
        self.home_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image: url(:/logo/Resources/ad-solid.svg);\n"
"font: 9pt \"微软雅黑\";")
        self.home_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/file_manager/Resources/file_manager/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_btn.setIcon(icon)
        self.home_btn.setObjectName("home_btn")
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(460, 240, 81, 31))
        self.refresh_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image: url(:/logo/Resources/ad-solid.svg);\n"
"font: 9pt \"微软雅黑\";")
        self.refresh_btn.setObjectName("refresh_btn")
        self.renameFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.renameFile_btn.setGeometry(QtCore.QRect(360, 240, 81, 31))
        self.renameFile_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.renameFile_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image: url(:/logo/Resources/ad-solid.svg);\n"
"font: 9pt \"微软雅黑\";")
        self.renameFile_btn.setObjectName("renameFile_btn")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(-50, -20, 721, 81))
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 399, 231, 20))
        self.line.setSizeIncrement(QtCore.QSize(0, 0))
        self.line.setStyleSheet("color: rgb(126, 126, 126);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(20, 399, 16, 20))
        self.line_5.setSizeIncrement(QtCore.QSize(0, 0))
        self.line_5.setStyleSheet("color: rgb(126, 126, 126);")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(310, 409, 20, 111))
        self.line_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.line_2.setStyleSheet("color: rgb(126, 126, 126);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 409, 20, 111))
        self.line_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.line_4.setStyleSheet("color: rgb(126, 126, 126);")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(41, 402, 54, 12))
        self.label_5.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(94, 94, 94);")
        self.label_5.setObjectName("label_5")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 509, 301, 20))
        self.line_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.line_3.setStyleSheet("color: rgb(126, 126, 126);")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 420, 71, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(362, 400, 81, 16))
        self.label_7.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(94, 94, 94);")
        self.label_7.setObjectName("label_7")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(341, 398, 16, 20))
        self.line_6.setSizeIncrement(QtCore.QSize(0, 0))
        self.line_6.setStyleSheet("color: rgb(126, 126, 126);")
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(550, 408, 20, 111))
        self.line_7.setSizeIncrement(QtCore.QSize(0, 0))
        self.line_7.setStyleSheet("color: rgb(126, 126, 126);")
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(440, 398, 121, 20))
        self.line_8.setSizeIncrement(QtCore.QSize(0, 0))
        self.line_8.setStyleSheet("color: rgb(126, 126, 126);")
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(330, 408, 20, 111))
        self.line_9.setSizeIncrement(QtCore.QSize(0, 0))
        self.line_9.setStyleSheet("color: rgb(126, 126, 126);")
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(340, 508, 221, 20))
        self.line_10.setSizeIncrement(QtCore.QSize(0, 0))
        self.line_10.setStyleSheet("color: rgb(126, 126, 126);")
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setObjectName("line_10")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(373, 445, 54, 12))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_8.setFont(font)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setObjectName("label_8")
        self.fileSize_data = QtWidgets.QLabel(self.centralwidget)
        self.fileSize_data.setGeometry(QtCore.QRect(193, 420, 121, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.fileSize_data.setFont(font)
        self.fileSize_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.fileSize_data.setObjectName("fileSize_data")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 445, 54, 12))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_10.setFont(font)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setObjectName("label_10")
        self.freeSpace_data = QtWidgets.QLabel(self.centralwidget)
        self.freeSpace_data.setGeometry(QtCore.QRect(348, 420, 101, 21))
        self.freeSpace_data.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(0, 121, 107);")
        self.freeSpace_data.setObjectName("freeSpace_data")
        self.used_data = QtWidgets.QLabel(self.centralwidget)
        self.used_data.setGeometry(QtCore.QRect(454, 420, 101, 21))
        self.used_data.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(0, 121, 107);")
        self.used_data.setObjectName("used_data")
        self.totalSpace_data = QtWidgets.QLabel(self.centralwidget)
        self.totalSpace_data.setGeometry(QtCore.QRect(348, 471, 101, 21))
        self.totalSpace_data.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(0, 121, 107);")
        self.totalSpace_data.setObjectName("totalSpace_data")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(377, 496, 54, 12))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_14.setFont(font)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_14.setObjectName("label_14")
        self.percent_data = QtWidgets.QLabel(self.centralwidget)
        self.percent_data.setGeometry(QtCore.QRect(455, 472, 101, 21))
        self.percent_data.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(0, 121, 107);")
        self.percent_data.setObjectName("percent_data")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(475, 492, 71, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_24.setFont(font)
        self.label_24.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_24.setObjectName("label_24")
        self.fileType_data = QtWidgets.QLabel(self.centralwidget)
        self.fileType_data.setGeometry(QtCore.QRect(193, 445, 121, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.fileType_data.setFont(font)
        self.fileType_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.fileType_data.setObjectName("fileType_data")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(130, 445, 71, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.fileEditdate_data = QtWidgets.QLabel(self.centralwidget)
        self.fileEditdate_data.setGeometry(QtCore.QRect(193, 470, 121, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.fileEditdate_data.setFont(font)
        self.fileEditdate_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.fileEditdate_data.setObjectName("fileEditdate_data")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(130, 470, 71, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_13.setObjectName("label_13")
        self.fileIcon = QtWidgets.QTextBrowser(self.centralwidget)
        self.fileIcon.setGeometry(QtCore.QRect(30, 420, 71, 71))
        self.fileIcon.setObjectName("fileIcon")
        self.fileName_data = QtWidgets.QLabel(self.centralwidget)
        self.fileName_data.setGeometry(QtCore.QRect(20, 494, 301, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.fileName_data.setFont(font)
        self.fileName_data.setObjectName("fileName_data")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(50, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.textBrowser_4.raise_()
        self.FileList.raise_()
        self.path_edit.raise_()
        self.label.raise_()
        self.goto_btn.raise_()
        self.textBrowser_2.raise_()
        self.label_16.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.textEdit_2.raise_()
        self.label_17.raise_()
        self.label_20.raise_()
        self.label_4.raise_()
        self.label_21.raise_()
        self.label_18.raise_()
        self.moveFile_btn.raise_()
        self.pasteFile_btn.raise_()
        self.delFile_btn.raise_()
        self.copyFile_btn.raise_()
        self.label_19.raise_()
        self.label_22.raise_()
        self.textEdit_3.raise_()
        self.upload.raise_()
        self.download_btn.raise_()
        self.home_btn.raise_()
        self.refresh_btn.raise_()
        self.renameFile_btn.raise_()
        self.line.raise_()
        self.line_5.raise_()
        self.line_4.raise_()
        self.label_5.raise_()
        self.line_3.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.line_9.raise_()
        self.line_10.raise_()
        self.label_8.raise_()
        self.fileSize_data.raise_()
        self.label_10.raise_()
        self.freeSpace_data.raise_()
        self.used_data.raise_()
        self.totalSpace_data.raise_()
        self.label_14.raise_()
        self.percent_data.raise_()
        self.label_24.raise_()
        self.fileType_data.raise_()
        self.label_11.raise_()
        self.fileEditdate_data.raise_()
        self.label_13.raise_()
        self.line_2.raise_()
        self.fileIcon.raise_()
        self.fileName_data.raise_()
        self.label_12.raise_()
        self.label_23.raise_()
        self.back_btn.raise_()
        FileMangerWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FileMangerWindow)
        QtCore.QMetaObject.connectSlotsByName(FileMangerWindow)

    def retranslateUi(self, FileMangerWindow):
        _translate = QtCore.QCoreApplication.translate
        FileMangerWindow.setWindowTitle(_translate("FileMangerWindow", "文件管理器"))
        self.label.setText(_translate("FileMangerWindow", ">"))
        self.delFile_btn.setText(_translate("FileMangerWindow", "删除"))
        self.upload.setText(_translate("FileMangerWindow", "上传文件"))
        self.copyFile_btn.setText(_translate("FileMangerWindow", "复制"))
        self.pasteFile_btn.setText(_translate("FileMangerWindow", "粘贴"))
        self.moveFile_btn.setText(_translate("FileMangerWindow", "移动"))
        self.download_btn.setText(_translate("FileMangerWindow", "下载文件"))
        self.goto_btn.setText(_translate("FileMangerWindow", "转到"))
        self.textBrowser_2.setHtml(_translate("FileMangerWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setWhatsThis(_translate("FileMangerWindow", "背景"))
        self.label_2.setText(_translate("FileMangerWindow", "<html><head/><body><p><img src=\":/file_manager/Resources/file_manager/folder.svg\"/></p></body></html>"))
        self.label_3.setText(_translate("FileMangerWindow", "当前位置"))
        self.textEdit_2.setHtml(_translate("FileMangerWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; color:#000000;\">文件操作</span></p></body></html>"))
        self.label_4.setText(_translate("FileMangerWindow", "远程文件"))
        self.textEdit_3.setHtml(_translate("FileMangerWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; color:#000000;\">传输操作</span></p></body></html>"))
        self.refresh_btn.setText(_translate("FileMangerWindow", "刷新"))
        self.renameFile_btn.setText(_translate("FileMangerWindow", "重命名"))
        self.label_5.setText(_translate("FileMangerWindow", "文件信息"))
        self.label_6.setText(_translate("FileMangerWindow", "文件大小："))
        self.label_7.setText(_translate("FileMangerWindow", "空间使用情况"))
        self.label_8.setText(_translate("FileMangerWindow", "可用空间"))
        self.fileSize_data.setText(_translate("FileMangerWindow", "无选中文件"))
        self.label_10.setText(_translate("FileMangerWindow", "已用空间"))
        self.freeSpace_data.setText(_translate("FileMangerWindow", "<html><head/><body><p align=\"center\">正在获取</p></body></html>"))
        self.used_data.setText(_translate("FileMangerWindow", "<html><head/><body><p align=\"center\">正在获取</p></body></html>"))
        self.totalSpace_data.setText(_translate("FileMangerWindow", "<html><head/><body><p align=\"center\">正在获取</p></body></html>"))
        self.label_14.setText(_translate("FileMangerWindow", "总空间"))
        self.percent_data.setText(_translate("FileMangerWindow", "<html><head/><body><p align=\"center\">正在获取</p></body></html>"))
        self.label_24.setText(_translate("FileMangerWindow", "已用空间 %"))
        self.fileType_data.setText(_translate("FileMangerWindow", "无选中文件"))
        self.label_11.setText(_translate("FileMangerWindow", "文件类型："))
        self.fileEditdate_data.setText(_translate("FileMangerWindow", "无选中文件"))
        self.label_13.setText(_translate("FileMangerWindow", "修改日期："))
        self.fileIcon.setHtml(_translate("FileMangerWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'微软雅黑\';\"><br /></p></body></html>"))
        self.fileName_data.setText(_translate("FileMangerWindow", "<html><head/><body><p align=\"center\">未选中文件</p></body></html>"))
        self.label_12.setText(_translate("FileMangerWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">文件管理器</span></p></body></html>"))