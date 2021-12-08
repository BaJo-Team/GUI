import sys

import os

from PySide2 import QtUiTools

from PySide2.QtWidgets import QApplication, QMainWindow

import single_File
import multi_File


class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setupUI()

    def setupUI(self):
        global UI_set

        UI_set = QtUiTools.QUiLoader().load(resource_path("main.ui"))

        UI_set.single_File.clicked.connect(self.open_single)
        UI_set.multi_File.clicked.connect(self.open_multi)

        self.setCentralWidget(UI_set)
        self.setWindowTitle("파일 변환 프로그램")
        self.resize(500, 270)
        self.show()

    #단일 변환 창 띄우기
    def open_single(self):
        self.S = single_File.MainView()

    #다중 변환 창 띄우기
    def open_multi(self):
        self.M = multi_File.MainView()

# 파일 경로
# pyinstaller로 원파일로 압축할때 경로 필요함
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainView()

    # main.show()

    sys.exit(app.exec_())