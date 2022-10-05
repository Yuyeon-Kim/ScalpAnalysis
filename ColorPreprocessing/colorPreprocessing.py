from email.mime import image
import cv2
import os
import re
# import numpy as np

def calc_bgr_mean(img)->tuple: # bgr 평균 값 계산 함수
    b, g, r = cv2.split(img)
    b_m, g_m, r_m = b.mean(), g.mean(), r.mean()
    return(b_m, g_m, r_m)

def calc_luminance_mean(img)->float:# 밝기 평균 값 계산 함수
    return(img.mean())


# 실행 시 아래의 3개 path들 지정
dataset_path = "F:/Datasets/scalpDatasets/AIHub/Validation"# 데이터셋 경로
result_folder_path = "F:/Datasets/scalpDatasets/AIHub_colorpreprocessed/Validation"# 전처리된 데이터 저장할 폴더 경로
standard_image_path = "ColorPreprocessing/test_images/0131_A2LEBJJDE00166C_1604675694014_3_TH.jpg" # 기준 이미지 경로

# 이미지 폴더/ 이미지 이름 읽기
# 주의사항: 이미지 폴더와 이미지는 영어와 _로만 이루어야함. cv 라이브러리에서 읽기 위함
image_folders = os.listdir(dataset_path)# 데이터셋 경로 지정, 이미지가 들어있는 폴더 이름을 모두 가져온다.

# 이미지 폴더 영어와 _ 로만 이루어지지 않은 것 제외
# 알맞은 경우 출력 폴더 생성
# 이미지 이름은 너무많아서 효율 위해 처리안함
reg = re.compile('[a-zA-Z_]+')
for i, i_f in enumerate(image_folders.copy()):
    if reg.match(i_f):# 알맞은 형태의 이름인가?
        os.makedirs(os.path.join(result_folder_path, i_f), exist_ok=True) # 폴더 생성
    else:
        image_folders.remove(i_f) # 삭제

image_names = [os.listdir(os.path.join(dataset_path, i_f)) for i_f in image_folders]# 이미지 각각의 경로를 2중 리스트 형태로

# 기준 이미지로 기준 값 계산 os.path.join()
s_img = cv2.imread(standard_image_path, cv2.IMREAD_COLOR)# 이미지 읽기
s_b_m, s_g_m, s_r_m = calc_bgr_mean(s_img)
s_fade = calc_luminance_mean(s_img)
# print(s_b_m, s_g_m, s_r_m)
# print(s_fade)

for i_f, i_ns in zip(image_folders, image_names):
    for i_n in i_ns:
        try:
            # 처리할 이미지로 처리 값 계산
            img = cv2.imread(os.path.join(dataset_path, i_f, i_n), cv2.IMREAD_COLOR)# 이미지 읽기
            img_b, img_g, img_r = calc_bgr_mean(img)
            img_fade = calc_luminance_mean(img)
            # print(img_b, img_g, img_r)
            # print(img_fade)

            # 이미지 색상 처리
            processed_img = cv2.add(img, (s_b_m-img_b+img_fade-s_fade, s_g_m-img_g+img_fade-s_fade, s_r_m-img_r+img_fade-s_fade, 0))

            # 전처리된 이미지 저장
            cv2.imwrite(os.path.join(result_folder_path, i_f, i_n), processed_img)

            # 이미지 출력
            # cv2.imshow('Standard', s_img)
            # cv2.imshow('Original', img)
            # cv2.imshow('Processed', processed_img)

            # cv2.waitKey(0) # 키 입력 있을때까지 기다림
            # cv2.destroyAllWindows()
        except ValueError as e:
            print("파일 경로가 한글이거나, 이미지 파일이 아닌지 확인해보세요.")
            print(e)