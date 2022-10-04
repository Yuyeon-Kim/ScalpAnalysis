import cv2
# import numpy as np

def calc_bgr_mean(img)->tuple: # bgr 평균 값 계산 함수
    b, g, r = cv2.split(img)
    b_m, g_m, r_m = b.mean(), g.mean(), r.mean()
    return(b_m, g_m, r_m)

def calc_luminance_mean(img)->float:# 밝기 평균 값 계산 함수
    return(img.mean())

# 기준 이미지로 기준 값 계산
s_img = cv2.imread('test_images/0131_A2LEBJJDE00166C_1604675694014_3_TH.jpg', cv2.IMREAD_COLOR)# 이미지 경로 설정
s_b_m, s_g_m, s_r_m = calc_bgr_mean(s_img)
s_fade = calc_luminance_mean(s_img)
# print(s_b_m, s_g_m, s_r_m)
# print(s_fade)

# 처리할 이미지로 처리 값 계산
img = cv2.imread('test_images/0643_A2LEBJJDE00048F_1606711282919_5_RH.jpg', cv2.IMREAD_COLOR)# 이미지 경로 설정
img_b, img_g, img_r = calc_bgr_mean(img)
img_fade = calc_luminance_mean(img)
print(img_b, img_g, img_r)
print(img_fade)

# 이미지 색상 처리
processed_img = cv2.add(img, (s_b_m-img_b+img_fade-s_fade, s_g_m-img_g+img_fade-s_fade, s_r_m-img_r+img_fade-s_fade, 0))

# 이미지 출력
cv2.imshow('Standard', s_img)
cv2.imshow('Original', img)
cv2.imshow('Processed', processed_img)

cv2.waitKey(0) # 키 입력 있을때까지 기다림
cv2.destroyAllWindows()