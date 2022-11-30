# ScalpAnalysis
두피 분석 개별연구

1. 피부 톤 일반화 (Normalize skin tone)  
  두피 데이터셋에서 조명에 따라 피부의 색이 달라진다. 그러나 이는 탈모 분석 시에 불리하게 작용한다. 따라서 이를 일정하게 되도록 조정하고자 하였다. 기준 이미지를 정해서 색감을 추출하고, 기준 이미지와 비슷한 색감을 가지도록 입력 이미지를 처리한다.  
  색감을 추출하는 알고리즘은 다음과 같다. 이미지의 R, G, B 값 각각에 대한 평균을 구해 "평균 R", "평균 G", "평균 B" 값을 구한다. 광도를 구하기 위해 전체 RGB 값의 평균을 구해 "광도"를 구한다. 이러한 "평균 R", "평균 G", "평균 B", "광도" 값이 색감의 지표가 된다.  
  입력 이미지를 처리하는 과정은 다음과 같다. 기준이 되는 이미지를 정한다. 본 데이터셋에서는 붉은색~푸른색의 스펙트럼 내에 피부 색이 존재함을 알았다. 따라서 중간값으로 판단된 살구색 이미지 ""를 기준 이미지로 선정했다. 기준 이미지에서 색감 추출 알고리즘으로 색감을 추출해 색감 지표를 구하고, 저장한다. 하나의 기준 이미지에 대해 여러개의 입력 이미지를 처리할 수 있다. 입력 이미지 각각에 대해 색감 추출 알고리즘으로 색감 지표를 구한다. 입력 이미지의 RGB 값에 기준 이미지와 입력 이미지의 색감 지표의 차를 더해서 처리한다.  
  [코드](ColorPreprocessing/colorPreprocessing.py)
  

2. 두피 특징에 맞춰서 붉은색 처리  
  [세부 내용 및 사용법](ColorPreprocessing/redTransform.md)  
  [코드](ColorPreprocessing/redTransform.py)  

3. pca augmentation  
  [세부 내용 및 사용법](PcaColorAugmentation/PcaColorAugmentation.md)  
  [코드](PcaColorAugmentation/fancy_pca.py)
