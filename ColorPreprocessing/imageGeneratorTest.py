import numpy as np
import pandas as pd
import os

import cv2
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.image  import ImageDataGenerator

# 이미지 불러오기
image = cv2.imread('ColorPreprocessing/test_images/0131_A2LEBJJDE00166C_1604282955299_4_LH.jpg')


# 좌우 반전 , 좌우반전을 True로 했지만 keras에서 랜덤으로 할 지 말 지 결정!..즉 좌우 반전 안 될 수도 있음.
# 좌우 상하 반전, 최대 45도 회전, 90%~110%확대 진행
data_generator = ImageDataGenerator(horizontal_flip=True, vertical_flip=True, rotation_range=0.45, zoom_range=[0.9, 1.1])

# opencv에서는 BGR 순이므로 BGR에서 RGB로 convertColor 해줌
image_batch = np.expand_dims(cv2.cvtColor(image,cv2.COLOR_BGR2RGB),axis=0) #4차원으로 늘려주기


# ImageDataGenerator 적용하려면 fit과 flow를 해야함.
data_generator.fit(image_batch)
data_gen_iter = data_generator.flow(image_batch)

#실행을 위해선 next 필요
aug_image_batch = next(data_gen_iter)

aug_image = np.squeeze(aug_image_batch)

aug_image = aug_image.astype('uint8')

# cv2 출력을 위해 BGR로 다시 변환
aug_image = cv2.cvtColor(aug_image, cv2.COLOR_RGB2BGR)

# 이미지 출력
cv2.imshow('Original', image)
cv2.imshow('Augmented', aug_image)

cv2.waitKey(0) # 키 입력 있을때까지 기다림
cv2.destroyAllWindows()

