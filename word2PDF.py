import os
import win32com.client as win32

# 단일 변환
def word2pdf(input_file_path, output_folder_path):
    # 가져온 파일의 이름
    file_name = input_file_path.split("\\")[-1].split(".")[0]
    # 저장할 파일 절대 경로
    output_file_path = os.path.join(output_folder_path, file_name + ".pdf")

    # 파일 미리 만들기
    file = open(output_file_path, "w")
    file.close()

    # word -> pdf
    application = win32.Dispatch('Word.Application')
    doc = application.Documents.Open(input_file_path)
    doc.SaveAs(output_file_path, 17)
    doc.Close()
    application.Quit()

    return file_name + ".pdf"

#워드 다중파일 변환
def word2pdfs(input_file_paths, output_folder_path):
    # 리스트로 내보낼 pdf 변환된 파일 이름들
    output_file_names = []

    # 선택된 파일들 하나하나 pdf로 변환(위에서 만든 함수 사용)
    for input_file_path in input_file_paths:
        # 경로 재구성
        input_file_path = change_path(input_file_path)
        # ppt -> word 변환
        output_file_name = word2pdf(input_file_path, output_folder_path)
        # 리스트에 pdf 변환된 파일 이름 추가
        output_file_names.append(output_file_name)

    return output_file_names

def change_path(path):
    new_path = path.replace('/', '\\')
    return new_path