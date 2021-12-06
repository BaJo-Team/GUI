import sys

import os

from PySide2 import QtUiTools, QtGui

from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget, QLabel, QVBoxLayout

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setupUI()

    def setupUI(self):
        global UI_set

        UI_set = QtUiTools.QUiLoader().load(resource_path("single_File.ui")) # ui파일 오픈

        UI_set.File_Select.clicked.connect(self.FindFile) #파일 찾기 버튼의 이벤트 연결
        UI_set.select_save_place.clicked.connect(self.select_save_place) #파일 저장위치 버튼의 이벤트 연결

        self.setCentralWidget(UI_set)
        self.setWindowTitle("단일 파일 변환")
        #self.setWindowIcon(QtGui.QPixmap(resource_path("./images/jbmpa.png")))
        self.resize(510, 350)
        self.show()

    def FindFile(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter(
            self.tr("All Files(*.*)"))
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            dirName = dialog.selectedFiles()
            self.fileName = dialog.selectedFiles()
            UI_set.current_File.setText("현재 파일" + self.fileName[0]) #현재 파일의 이름과 경로를 출력

            #파일의 절대 경로를 받아서 파일명을 지우고 파일의 디렉토리를 추출해서 저장경로에 보여줌
            save = str(dirName)[1:-1].split("/") #파일의 절대경로
            del save[-1] #파일명 삭제 
            place='/'.join(save) #문자열을 리스트로 변경
            UI_set.show_save_place.setText("저장경로:"+str(place)) #출력

    #파일 저장 경로 지정 함수
    def select_save_place(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            dirName = dialog.selectedFiles()
            UI_set.show_save_place.setText("저장경로:\n" + str(dirName)[1:-1]) # 앞과 뒤의 [,]를 삭제하고 출력

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