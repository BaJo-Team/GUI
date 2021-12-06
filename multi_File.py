import sys

import os

from PySide2 import QtUiTools

from PySide2.QtWidgets import QApplication, QMainWindow

from PySide2.QtWidgets import QFileDialog


class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setupUI()

    def setupUI(self):
        global UI_set

        UI_set = QtUiTools.QUiLoader().load(resource_path("multi_File.ui")) #ui파일 오픈

        UI_set.Find_File.clicked.connect(self.Find_multi_File) #파일 찾기 버튼의 이벤트 연결
        UI_set.select_save_place.clicked.connect(self.select_save_place) #파일 저장위치 버튼의 이벤트 연결

        self.setCentralWidget(UI_set)
        self.setWindowTitle("다중 파일 변환")
        #self.setWindowIcon(QtGui.QPixmap(resource_path("./images/jbmpa.png")))
        self.resize(500, 270)
        self.show()

    def Find_multi_File(self):
        UI_set.show_selected_Files.clear() # TextBrowser의 내용 삭제 (내용 비우기)
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setNameFilter(
            self.tr("All Files(*.*)"))
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            strofFile = str(fileNames)[1:-1].split(",") #파일들의 경로와 이름을 받아서 리스트로 스플릿

            for name in strofFile:
                UI_set.show_selected_Files.append(name) #리스트를 처음부터 순차적으로 모두 출력

    def select_save_place(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            dirName = dialog.selectedFiles()
            UI_set.show_save_place.clear()  # TextBrowser의 내용 삭제 (내용 비우기)
            UI_set.show_save_place.append("저장경로:\n"+str(dirName)[1:-1]) # 앞과 뒤의 [,]을 삭제하고 출력

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