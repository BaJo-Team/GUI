import os
import win32com.client as win32
import win32gui


# 단일 변환
def hwp2pdf(input_file_path, output_folder_path):
    file_name = input_file_path.split("\\")[-1].split(".")[0]  # 선택한 파일 이름
    output_file_path = os.path.join(output_folder_path, file_name + ".pdf")  # 변환된 파일 저장 경로

    hwp = win32.gencache.EnsureDispatch('HWPFrame.HwpObject')  # 한/글 열기
    hwnd = win32gui.FindWindow(None, '빈 문서 1 - 한글')

    hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")  # 한글 보안창 삭제

    win32gui.ShowWindow(hwnd, 0)

    hwp.Open(input_file_path)
    hwp.HAction.GetDefault('FileSaveAsPdf', hwp.HParameterSet.HFileOpenSave.HSet)
    hwp.HParameterSet.HFileOpenSave.filename = output_file_path
    hwp.HParameterSet.HFileOpenSave.Format = 'PDF'
    hwp.HAction.Execute('FileSaveAsPdf', hwp.HParameterSet.HFileOpenSave.HSet)

    win32gui.ShowWindow(hwnd, 5)
    hwp.XHwpDocuments.Close(isDirty=False)
    hwp.Quit()

    return file_name + ".pdf"


# 다중 변환
def hwp2pdfs(input_file_paths, output_folder_path):
    # 리스트로 내보낼 pdf 변환된 파일 이름들
    output_file_names = []

    for input_file_path in input_file_paths:
        # img -> pdf
        output_file_name = hwp2pdf(change_path(input_file_path), change_path(output_folder_path))
        # 리스트에 pdf 변환된 파일 이름 추가
        output_file_names.append(output_file_name)

    return output_file_names


def change_path(path):
    new_path = path.replace('/', '\\')
    return new_path
