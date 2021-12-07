import os
import win32com.client as win32

# 단일 파일
def ppt2pdf(input_file_path, output_folder_path):
    # 가져온 파일의 이름
    file_name = input_file_path.split("\\")[-1].split(".")[0]
    # 저장할 파일 절대 경로
    output_file_path = os.path.join(output_folder_path, file_name + ".pdf")
    # win32모듈로 powerpoint.application 열기
    application = win32.Dispatch("Powerpoint.Application")
    # 선택한 powerpoint 파일 열기
    presentation = application.Presentations.Open(input_file_path, ReadOnly=False)
    # powerpoint -> pdf 변환
    presentation.SaveAs(output_file_path, 32)
    # powerpoint.application 닫기
    application.Quit()

    return file_name + ".pdf"

# 다중 파일
def ppt2pdfs(input_file_paths, output_folder_path):
    # 리스트로 내보낼 pdf 변환된 파일 이름들
    output_file_names = []

    # 선택된 파일들 하나하나 pdf로 변환(위에서 만든 함수 사용)
    for input_file_path in input_file_paths:
        # 경로 재구성
        input_file_path = change_path(input_file_path)
        # ppt -> pdf 변환
        output_file_name = ppt2pdf(input_file_path, output_folder_path)
        # 리스트에 pdf 변환된 파일 이름 추가
        output_file_names.append(output_file_name)

    return output_file_names

def change_path(path):
    new_path = path.replace('/', '\\')
    return new_path