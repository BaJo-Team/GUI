import sys

import os

from PySide2 import QtUiTools, QtGui

from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget, QLabel, QVBoxLayout

from word2PDF import word2pdf
from excel2PDF import excel2pdf
from hwp2PDF import hwp2pdf
from ppt2PDF import ppt2pdf
from img2PDF import img2pdf

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        global UI_set

        UI_set = QtUiTools.QUiLoader().load(resource_path("single_File.ui")) # ui파일 오픈

        UI_set.File_Select.clicked.connect(self.FindFile) #파일 찾기 버튼의 이벤트 연결
        UI_set.select_save_place.clicked.connect(self.select_save_place) #파일 저장위치 버튼의 이벤트 연결
        UI_set.change_File.clicked.connect(self.connect_File)

        self.setCentralWidget(UI_set)
        self.setWindowTitle("단일 파일 변환")
        self.resize(400, 300)
        self.show()

    def FindFile(self):
        value = UI_set.Select_File_type_2.currentText()

        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        if value == "hwp":
            dialog.setNameFilter(self.tr("Data Files (*.hwp);; All Files(*.*)"))
        elif value == "excel":
            dialog.setNameFilter(self.tr("Data Files (*.xlsx);; All Files(*.*)"))
        elif value == "img":
            dialog.setNameFilter(self.tr("Data Files (*.png *.xpm *.jpg *.gif);; All Files(*.*)"))
        elif value == "word":
            dialog.setNameFilter(self.tr("Data Files (*.dox *.docx);; All Files(*.*)"))
        elif value == "ppt":
            dialog.setNameFilter(self.tr("Data Files (*.ppt *.pptx);; All Files(*.*)"))


        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.fileName = dialog.selectedFiles()
            UI_set.current_File.setText(self.fileName[0].split("/")[-1]) #현재 파일의 이름과 경로를 출력

    #파일 저장 경로 지정 함수
    def select_save_place(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.dirName = dialog.selectedFiles()
            UI_set.show_save_place.setText(self.dirName[0])

    def connect_File(self):
        value = UI_set.Select_File_type_2.currentText()

        try:
            if(value == 'hwp'):
                self.result = hwp2pdf(change_path(self.fileName[0]),change_path(self.dirName[0]))
            elif(value == 'excel'):
                self.result = excel2pdf(change_path(self.fileName[0]),change_path(self.dirName[0]))
            elif(value == 'img'):
                self.result = img2pdf(change_path(self.fileName[0]),change_path(self.dirName[0]))
            elif(value == 'word'):
                self.result = word2pdf(change_path(self.fileName[0]),change_path(self.dirName[0]))
            elif(value == 'ppt'):
                self.result = ppt2pdf(change_path(self.fileName[0]),change_path(self.dirName[0]))
        except AttributeError:
            UI_set.show_result.setText("디렉토리와 파일 모두 선택하십시오.")

        UI_set.show_result.setText(self.result)

def change_path(path):
    new_path = path.replace('/', '\\')
    return new_path

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