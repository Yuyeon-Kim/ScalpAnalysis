redTransform.py 코드 설명
=============

필요한 라이브러리
--------------
- os
- openCV(cv2)
- random

코드 목적
--------------
1. 붉은색, 노란색, 살구색, 초록색, 파란색 의 스펙트럼 내의 사진의 색을 일정하게 보정
2. 위와 같은 방법으로 색 보정이 붉은색의 경우 잘 되지 않아 사용자가 설정한 퍼센트만큼 붉은 색을 첨가

알고리즘
--------------
1. 기준 이미지에서 R, G, B 각각의 값의 평균을 계산해 평균 R, 평균 G, 평균 B 값인 s_r_m, s_g_m, s_b_m를 계산
2. 기준 이미지의 모든 RGB 값의 평균으로 광도인 s_fade를 계산 
3. 처리 이미지에도 1.와 같은 방법으로 평균 R, 평균 G, 평균 B 값인 img_r, img_b, img_c를 계산
4. 처리 이미지에도 2.와 같은 방법으로 광도 img_fade를 계산
5. 처리 이미지에 R, G, B 값에 각각 기준 이미지와 처리 이미지의 RGB 평균 값 차이 및 기준 이미지와 처리 이미지의 광도 차이 값을 더해서 처리한다.
6. 기준 이미지 평균  R값에 사용자가 지정한 퍼센트 내에서 랜덤으로 값을 선정한다.
7. 처리 이미지의 R 값을 6.의 값을 더한다.
8. 사용자가 입력한 출력 이미지의 개수만큼 3.~7.의 과정을 반복한다.

함수 사용법
--------------
- redTransformer(reference_image_path: str, processing_image_path: str, N: int = 5, raito1 = [-0.2, 0.2])
기준 이미지 경로, 처리 이미지 경로, 출력 이미지 개수, 붉은 색 처리 정도[float, float]

- 사용 예제
  * 결과 출력 및 결과 저장은 사용 목적에 따라 주석처리하여 일부만 사용하면 된다.

```
reference_image_path = "ColorPreprocessing/test_images/0131_A2LEBJJDE00166C_1604675694014_3_TH.jpg" # 기준 이미지 경로
processing_image_path= "ColorPreprocessing/test_images/0131_A2LEBJJDE00166C_1604675694014_3_TH.jpg" # 처리 이미지 경로

N = 5 # 출력하고자 하는 이미지의 수

raito1 = [-0.2, 0.2] # 처리를 원하는 하한 퍼센트, 상한 퍼센트 

result_imgs = redTransformer(reference_image_path, processing_image_path, N, raito1) # 붉은색 처리


save_file_path = "경로 지정" # 결과 저장 시에만 필요, 저장 "폴더" 경로 지정

for i, r_i in enumerate(result_imgs):
    # 결과 출력
    cv2.imshow('Random Processed %d' %i, r_i)
    cv2.waitKey(0) # 키 입력 있을때까지 기다림
    cv2.destroyAllWindows()

    # 결과 저장
    cv2.imwrite(os.path.join(save_file_path, "processed_img%d.jpg"%i), r_i)
```