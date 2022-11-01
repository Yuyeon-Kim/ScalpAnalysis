# import sys

import cv2
import random
# import numpy as np

def calc_bgr_mean(img)->tuple: # bgr 평균 값 계산 함수
    b, g, r = cv2.split(img)
    b_m, g_m, r_m = b.mean(), g.mean(), r.mean()
    return(b_m, g_m, r_m)

def calc_luminance_mean(img)->float:# 밝기 평균 값 계산 함수
    return(img.mean())

def redTransformer(reference_image_path, processing_image_path, raito1, raito2): # raito1: [float, float], raito2: [float, float, ...]
    # 기준 이미지로 기준 값 계산
    s_img = cv2.imread(reference_image_path, cv2.IMREAD_COLOR)# 이미지 경로 설정
    s_b_m, s_g_m, s_r_m = calc_bgr_mean(s_img)
    s_fade = calc_luminance_mean(s_img)
    print("s_b_m, s_g_m, s_r_m:", s_b_m, s_g_m, s_r_m)
    print("s_fade:",s_fade)

    # 처리할 이미지로 처리 값 계산
    img = cv2.imread(processing_image_path, cv2.IMREAD_COLOR)# 이미지 경로 설정
    img_b, img_g, img_r = calc_bgr_mean(img)
    img_fade = calc_luminance_mean(img)
    print("img_b, img_g, img_r",img_b, img_g, img_r)
    print("img_fade",img_fade)


    # 붉은 색 처리 방법 1. 랜덤 함수 사용, 기준 파일의 Red 수치(int) 의 +-20% 내에서 붉은 색을 더하거나 뺌
    red_random = random.randrange(int(s_r_m*raito1[0]), int(s_r_m*raito1[1])) 
    print("red_random:", red_random)

    # 붉은 색 처리 방법 2. 리스트 사용, 기준 파일의 Red 수치(int)의 -20%, -10%, 0%, 10%, 20% 값만큼 붉은 색을 더하거나 뺌
    temp = [s_r_m*i for i in raito2]
    red_list = list(map(int, temp))

    # 붉은 색 처리 방법 3. 붉은 색 값이 제일 높은 경우에만 붉은 색을 낮춰서..?

    # 이미지 색상 처리
    # 방법 1
    processed_img = cv2.add(img, (s_b_m-img_b+img_fade-s_fade, s_g_m-img_g+img_fade-s_fade, s_r_m+red_random-img_r+img_fade-s_fade, 0)) # 붉은 색에만 랜덤으로 처리

    # 이미지 출력
    cv2.imshow('Standard', s_img)
    cv2.imshow('Original', img)
    cv2.imshow('Processed Random', processed_img)

    cv2.waitKey(0) # 키 입력 있을때까지 기다림
    cv2.destroyAllWindows()


    # 방법 2
    for r_l in red_list:
        processed_img = cv2.add(img, (s_b_m-img_b+img_fade-s_fade, s_g_m-img_g+img_fade-s_fade, s_r_m+r_l-img_r+img_fade-s_fade, 0))
        # 이미지 출력
        cv2.imshow('Standard', s_img)
        cv2.imshow('Original', img)
        cv2.imshow('Processed '+str(r_l), processed_img)

        cv2.waitKey(0) # 키 입력 있을때까지 기다림
        cv2.destroyAllWindows()




def main():
    pass

if __name__ == "__main__":
    main()
    # redTransformer(sys.argv[1], sys.argv[2], list(map(float, sys.argv[3])), list(map(float, sys.argv[4])))
    reference_image_path = "ColorPreprocessing/test_images/0131_A2LEBJJDE00166C_1604675694014_3_TH.jpg"
    processing_image_path= "ColorPreprocessing/test_images/0131_A2LEBJJDE00166C_1604675694014_3_TH.jpg"

    raito1 = [-0.2, 0.2]
    raito2 = [-0.2+i/10 for i in range(5)]
    print(raito1)
    print(raito2)

    redTransformer(reference_image_path, processing_image_path, raito1, raito2)