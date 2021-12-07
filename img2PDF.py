import os
from PIL import Image

# 단일 파일 변환
def img2pdf(input_file_path, output_folder_path):
    # 가져온 파일의 이름
    file_name = input_file_path.split("\\")[-1].split(".")[0]
    # 저장할 파일 절대 경로
    output_file_path = os.path.join(output_folder_path, file_name + ".pdf")
    # img -> pdf
    img = Image.open(input_file_path)
    imgConvert = img.convert('RGB')
    imgConvert.save(output_file_path)

    return file_name + ".pdf"

# 다중 파일 변환
def img2pdfs(input_file_paths, output_folder_path):
    # 리스트로 내보낼 pdf 변환된 파일 이름들
    output_file_names = []

    # 선택된 파일들 하나하나 pdf로 변환
    for input_file_path in input_file_paths:
        # img -> pdf
        output_file_name = img2pdf(input_file_path, output_folder_path)
        # 리스트에 pdf 변환된 파일 이름 추가
        output_file_names.append(output_file_name)

    return output_file_names

# 여러개의 이미지 파일을 하나의 pdf 파일로 만들기
def imgs2pdf(input_file_paths, output_folder_path):
    # 가져온 파일의 이름
    file_name = ""

    img_list = []
    for input_file_path in input_file_paths:
        # 경로 재구성
        input_file_path = change_path(input_file_path)
        file_name += input_file_path.split("\\")[-1].split(".")[0]

        img = Image.open(input_file_path)
        img.convert("RGB")
        img_list.append(img)

    # 저장할 파일 절대 경로
    output_file_path = os.path.join(output_folder_path, file_name + ".pdf")
    img_list[0].save(output_file_path, save_all=True, append_images=img_list)

    return file_name

def change_path(path):
    new_path = path.replace('/', '\\')
    return new_path