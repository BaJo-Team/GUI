import os
import win32com.client as win32
import win32gui


# 단일 변환
def hwp2pdf(input_file_path, output_folder_path):
    file_name = input_file_path.split("\\")[-1].split(".")[0]  # 선택한 파일 이름
    output_file_path = os.path.join(output_folder_path, file_name + ".pdf")  # 변환된 파일 저장 경로

    hwp = win32.gencache.EnsureDispatch('HWPFrame.HwpObject')  # 한/글 열기
    hwnd = win32gui.FindWindow(None, '빈 문서 1 - 한글')

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
def hwps2pdfs(input_file_paths, output_folder_path):
    file_names = []  # 선택한 파일들의 이름 리스트
    output_file_paths = []  # 변환된 파일들 저장 경로
    output_file_names = []  # 변환된 파일들 이름

    for i in range(len(input_file_paths)):  #
        file_name = input_file_paths[i].split("\\")[-1].split(".")[0]
        file_names.append(file_name)
        output_file_path = os.path.join(output_folder_path, file_name + ".pdf")
        output_file_paths.append(output_file_path)
        output_file_name = output_file_path.split("\\")[-1].split(".")[0]
        output_file_names.append(output_file_name)

    hwp = win32.gencache.EnsureDispatch('HWPFrame.HwpObject')  # 한/글 열기
    hwnd = win32gui.FindWindow(None, '빈 문서 1 - 한글')

    win32gui.ShowWindow(hwnd, 0)

    for input_file_path in input_file_paths:
        # 경로 재구성
        input_file_path = change_path(input_file_path)

        i = input_file_paths.index(input_file_path)  # 해당 파일 인덱스

        if not input_file_path.lower().endswith((".hwp")):  # 사용자가 .hwp 파일을 선택하지 않았을 경우
            continue

        hwp.Open(os.path.join(input_file_path))
        hwp.HAction.GetDefault('FileSaveAsPdf', hwp.HParameterSet.HFileOpenSave.HSet)
        hwp.HParameterSet.HFileOpenSave.filename = output_file_paths[i]  # output_folder_path에 변환된 pdf 파일 저장
        hwp.HParameterSet.HFileOpenSave.Format = 'PDF'
        hwp.HAction.Execute('FileSaveAsPdf', hwp.HParameterSet.HFileOpenSave.HSet)

    win32gui.ShowWindow(hwnd, 5)
    hwp.XHwpDocuments.Close(isDirty=False)
    hwp.Quit()

    return output_file_names

def change_path(path):
    new_path = path.replace('/', '\\')
    return new_path