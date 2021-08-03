# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication

from Ui.Resources import *
from Form.FileManagerForm import FileManagerForm


def fileManagerFormOpen():
    fileManagerForm.fileIcon.setHtml(_translate("FileMangerWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/file_type/Resources/file_type/folder.svg\" /></p></body></html>"))
    fileManagerForm.getFiles()
    fileManagerForm.getSpaceThread.start()  # 启动线程
    fileManagerForm.show()

def fileManagerFormClose():
    exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    _translate = QtCore.QCoreApplication.translate
    fileManagerForm = FileManagerForm()
    fileManagerFormOpen()
    # 文件管理器窗口按钮事件
    fileManagerForm.back_btn.clicked.connect(fileManagerFormClose)
    fileManagerForm.goto_btn.clicked.connect(fileManagerForm.goto)
    fileManagerForm.home_btn.clicked.connect(fileManagerForm.goHomeDir)
    fileManagerForm.refresh_btn.clicked.connect(fileManagerForm.refresh)
    fileManagerForm.copyFile_btn.clicked.connect(fileManagerForm.copyFile)
    fileManagerForm.moveFile_btn.clicked.connect(fileManagerForm.moveFile)
    fileManagerForm.pasteFile_btn.clicked.connect(fileManagerForm.pasteFile)
    fileManagerForm.renameFile_btn.clicked.connect(fileManagerForm.renameFile)
    fileManagerForm.delFile_btn.clicked.connect(fileManagerForm.delFile)
    fileManagerForm.download_btn.clicked.connect(fileManagerForm.downloadFile)
    fileManagerForm.upload.clicked.connect(fileManagerForm.uploadFile)
    # 重命名窗口按钮事件
    fileManagerForm.renameForm.ok_btn.clicked.connect(fileManagerForm.renameFileDo)
    fileManagerForm.renameForm.back_btn.clicked.connect(fileManagerForm.renameForm.hide)
    sys.exit(app.exec_())