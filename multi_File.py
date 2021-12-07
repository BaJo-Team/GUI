import sys

import os

from PySide2 import QtUiTools

from PySide2.QtWidgets import QApplication, QMainWindow

from PySide2.QtWidgets import QFileDialog

from word2PDF import word2pdfs
from excel2PDF import excel2pdfs
from hwp2PDF import hwp2pdfs
from ppt2PDF import ppt2pdfs
from img2PDF import img2pdfs

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        global UI_set

        UI_set = QtUiTools.QUiLoader().load(resource_path("multi_File.ui")) #ui파일 오픈

        UI_set.File_Select.clicked.connect(self.Find_multi_File) #파일 찾기 버튼의 이벤트 연결
        UI_set.select_save_place.clicked.connect(self.select_save_place) #파일 저장위치 버튼의 이벤트 연결
        UI_set.change_File.clicked.connect(self.connect_File)

        self.setCentralWidget(UI_set)
        self.setWindowTitle("다중 파일 변환")
        self.resize(400, 300)
        self.show()

    def Find_multi_File(self):
        UI_set.show_selected_Files.clear() # TextBrowser의 내용 삭제 (내용 비우기)
        value = UI_set.Select_File_type_2.currentText()
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFiles)
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
            self.fileNames = dialog.selectedFiles()

            for name in self.fileNames:
                UI_set.show_selected_Files.append(name.split("/")[-1]) #리스트를 처음부터 순차적으로 모두 출력

    def select_save_place(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.dirName = dialog.selectedFiles()
            UI_set.show_save_place.clear()  # TextBrowser의 내용 삭제 (내용 비우기)
            UI_set.show_save_place.append(self.dirName[0]) # 앞과 뒤의 [,]을 삭제하고 출력

    def connect_File(self):
        value = UI_set.Select_File_type_2.currentText()

        try:
            if(value == 'hwp'):
                result = hwp2pdfs(self.fileNames,change_path(self.dirName[0]))
            elif(value == 'excel'):
                result = excel2pdfs(self.fileNames,change_path(self.dirName[0]))
            elif(value == 'img'):
                result = img2pdfs(self.fileNames,change_path(self.dirName[0]))
            elif(value == 'word'):
                result = word2pdfs(self.fileNames,change_path(self.dirName[0]))
            elif(value == 'ppt'):
                result = ppt2pdfs(self.fileNames,change_path(self.dirName[0]))
        except AttributeError:
            UI_set.show_result.setText("디렉토리와 파일 모두 선택하십시오.")

        Line = ""
        for re in result:
            Line += re.split("/")[-1] +"\n"

        UI_set.show_result.setText(Line)

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