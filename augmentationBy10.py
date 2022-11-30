import os
import os.path
import cv2
import random
import glob
import numpy as np
from PcaColorAugmentation import fancy_pca

# bgr 평균 값 계산 함수
def calc_bgr_mean(img)->tuple: 
    b, g, r = cv2.split(img)
    b_m, g_m, r_m = b.mean(), g.mean(), r.mean()
    return(b_m, g_m, r_m)

# 밝기 평균 값 계산 함수
def calc_luminance_mean(img)->float:
    return(img.mean())

# raito1: [float, float]
def redTransformer(reference_image_path: str, input_image_path: str, N: int = 5, raito1 = [-0.2, 0.2]): 

    s_img = cv2.imread(reference_image_path, cv2.IMREAD_COLOR)  # 이미지 경로 설정
    img = cv2.imread(input_image_path, cv2.IMREAD_COLOR)    # 이미지 경로 설정

    return redTransformer(s_img, img, N, raito1)


# raito1: [float, float]
def redTransformer(reference_image: np.ndarray, input_image: np.ndarray, N: int = 5, raito1 = [-0.2, 0.2]): 

    if(len(raito1)!=2):
        print("raito1 자리에 [float, float] 형태의 값을 입력해주세요.")
    
    if(raito1[0]>raito1[1]):
        print("raito1 리스트의 0 인덱스의 값은 1 인덱스의 값보다 작게 입력하세요.")

    result = []

    # 기준 이미지로 기준 값 계산
    s_img = reference_image  # 이미지 경로 설정
    s_b_m, s_g_m, s_r_m = calc_bgr_mean(s_img)
    s_fade = calc_luminance_mean(s_img)

    # 처리할 이미지로 처리 값 계산
    img = input_image    # 이미지 경로 설정
    img_b, img_g, img_r = calc_bgr_mean(img)
    img_fade = calc_luminance_mean(img)

    for _ in range(N):
        # 붉은 색 처리 방법 1. 랜덤 함수 사용, 기준 파일의 Red 수치(int) 의 % raito1[0]~raito1[1] 내에서 붉은 색을 더하거나 뺌
        # + 1개 입력 ->  N개 출력
        red_random = random.randrange(int(s_r_m*raito1[0]), int(s_r_m*raito1[1])) 

        # 이미지 색상 처리
        processed_img = cv2.add(img, (s_b_m-img_b+img_fade-s_fade, s_g_m-img_g+img_fade-s_fade, s_r_m+red_random-img_r+img_fade-s_fade, 0)) # 붉은 색에만 랜덤으로 처리

        result.append(processed_img) # 출력 배열에 추가
    
    return result


if __name__ == "__main__":
    path = "/home/irteam/Skin-Analyzer/aihub_Efficient/model6/train"

    # 기준 이미지
    reference_image_path = "ColorPreprocessing/test_images/0131_A2LEBJJDE00166C_1604675694014_3_TH.jpg"

    # 입력 이미지
    input_path = "F:/Datasets/scalpDatasets/AIHub"
    input_image_path = [] 
    input_image_path.append(input_path + "/Training/alopecia_0")
    input_image_path.append(input_path + "/Training/alopecia_1")
    input_image_path.append(input_path + "/Training/alopecia_2")
    input_image_path.append(input_path + "/Training/alopecia_3")

    # 출력 이미지
    output_path = "F:/Datasets/scalpDatasets/AIHub/Preprocess/preprocess6"
    output_image_path = [] 
    output_image_path.append(output_path + "/Training/alopecia_0/")
    output_image_path.append(output_path + "/Training/alopecia_1/")
    output_image_path.append(output_path + "/Training/alopecia_2/")
    output_image_path.append(output_path + "/Training/alopecia_3/")
    print(output_image_path)

    # RedTransformer 파라미터 설정
    N = 5 # 출력하고자 하는 이미지의 수
    raito1 = [-0.2, 0.2] # 처리를 원하는 하한 퍼센트, 상한 퍼센트 

    # PCA Augmentation 파라미터 설정
    alpha = 0.3 # 분산 설정

    for index in range(4):
        for filename in os.listdir(str(input_image_path[index])):
            input_dir = str(input_image_path[index]) + "/" + filename
            reference_image = cv2.imread(reference_image_path, cv2.IMREAD_COLOR)  # 기준 이미지 불러오기
            input_image = cv2.imread(input_dir, cv2.IMREAD_COLOR)    # 입력(처리) 이미지 불러오기

            # RedTransformer 
            result_imgs = redTransformer(reference_image, input_image, N, raito1) # 붉은색 처리
            
            # PCA Augmentation
            for red_image in result_imgs.copy():
                pca_result_image = fancy_pca.fancy_pca(input_image, alpha) # pca augmentation
                result_imgs.append(pca_result_image)


            # 결과 저장 시에만 필요, 저장 "폴더" 경로 지정
            result_path = output_image_path[index]
            for i, r_i in enumerate(result_imgs):
                # 결과 저장
                this_path = result_path + os.path.splitext(filename)[0] + "_" + str(i) + ".jpg"
                cv2.imwrite(this_path, r_i)