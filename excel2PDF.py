import os
import pywintypes   # 엑셀 파일 에러
import win32com.client as win32

# 단일 파일
def excel2pdf(input_file_path, output_folder_path):
    # 가져온 파일의 이름
    file_name = input_file_path.split("\\")[-1].split(".")[0]
    # 저장할 파일 절대 경로
    output_file_path = os.path.join(output_folder_path, file_name + ".pdf")
    # win32모듈로 excel.application 열기
    application = win32.Dispatch("Excel.Application")
    # 선택한 excel 파일 열기
    excel = application.Workbooks.Open(input_file_path, ReadOnly=False)
    # excel -> pdf 변환 (+ 에러 처리)
    try:
        # pdf로 저장
        excel.ActiveSheet.ExportAsFixedFormat(0, output_file_path)
    except pywintypes.com_error:    # 엑셀 파일에 내용이 없을 때 에러 처리
        print("선택한 엑셀 파일에 변환할 내용이 없습니다.")
    # excel.application 닫기
    application.Quit()

    return file_name+".pdf"

# 다중 파일
def excel2pdfs(input_file_paths, output_folder_path):
    # 리스트로 내보낼 pdf 변환된 파일 이름들
    output_file_names = []

    # 선택된 파일들 하나하나 pdf로 변환(위에서 만든 함수 사용)
    for input_file_path in input_file_paths:
        # 경로 재구성
        input_file_path = change_path(input_file_path)
        # word -> pdf 변환
        output_file_name = excel2pdf(input_file_path, output_folder_path)
        # 리스트에 pdf 변환된 파일 이름 추가
        output_file_names.append(output_file_name)

    return output_file_names

# 경로 재구성
def change_path(path):
    new_path = path.replace('/', '\\')
    return new_path
