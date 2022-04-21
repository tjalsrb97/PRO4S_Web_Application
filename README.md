# 2021년 산학연계 프로젝트
# 밀집 도심지에서의 5세대 이동통신 기지국 최적화를 위한 밀리미터파 경로손실 딥러닝 모델 개발  
- 산혁연계 기업 : LG U+  
- 담당 : 이혁준 교수님(CINe Lab), 이지훈 조교님    
- 팀장 : 진우빈(ubinjin2@naver.com)  
- 목표 :
 1. 기존 경로손실 모델 대비 경제적이고, 높은 정확도를 가지는 모델 개발
 2. 이를 활용할 수 있는 웹 어플리케이션 개발
- 성과 :  
 3D ray tracing의 3D 모델링 평균 기간인 2.5일보다 빠르게 평균 2 시간 이내로 예측  
 1.8 GHz 대역 CNN 모델의 예측 정확도 수준에 도달 (RMSE: 5.3186 이하, Absolute Error: 2dB이하에서 38.33%, 5dB이하에서 77.97%, 10dB이하에서 98.05%)  
 모델 일반화를 통해 타 모델보다 유사 지형에 대한 예측 속도를 50%이상 단축  

![image](https://user-images.githubusercontent.com/42092864/120883080-278c0500-c616-11eb-8bee-07cacbc869f4.png "예측 결과 예시")  

---

## 1. 소개

밀집 도심지에서의 5세대 이동통신 기지국 설치 최적화를 위한 밀리미터파 경로손실 딥러닝 모델을 개발하였습니다.  
본 레포지토리는 딥러닝 모델을 이용하여 경로손실 예측을 시각화 한 웹 어플리케이션입니다.  

> 사용된 대표적인 프레임워크/라이브러리 Tensorflow, Mysql, Django, leaflet  

### 1.1 필요성?
- 5세대 밀리미터파 기술의 경제적 중요성  
- 5세대 밀리미터파 기술의 산업적 중요성  
- 경로손실 모델의 연구 중요성  

경제적, 산업적 의미가 큰 5세대 밀리미터파 서비스를 안정적이고, 신속하게 제공하기 위해    
본 프로젝트에선 새로운 5세대 밀리미터파 경로손실 모델과 이를 활용하는 웹어플리케이션을 구현하고자 했습니다.  

## 2. 개발내용
- 딥러닝 모델의 입력을 위한 학습 입력 이미지 생성 알고리즘 연구 및 개발
- 딥러닝 모델과 전파 실측정 데이터와 비교, 검증으로 모델 성능 개선 및 최적화
- 기존 전파 예측 방법론보다 적은 수행시간, 높은 정확성을 갖는 딥러닝 모델 구현
- 실무에서 적용이 가능한 오차 내의 에러율을 가지는 밀리미터파 딥러닝 모델 구현
- 최종 모델의 측정속도 가속화 및 가시화를 위한 최적화 서버 구축
- 웹 어플리케이션 구동을 위한 MPA 개발
- 이용 편의를 위한 UI 구현 및 전파 예측 결과 가시화 모듈 구현
- 웹 어플리케이션 결과 검증 및 관리를 위한 데이터베이스 구축


![image](https://user-images.githubusercontent.com/42092864/164551064-fc98a059-6a92-452d-830c-b45c14c88a39.png "구조 설계")  

![image](https://user-images.githubusercontent.com/42092864/164551150-9b6eb7d8-4492-4387-a3d6-59a9c32ddacf.png "상세 설계")


### 2.1 3D LAMS 알고리즘
지도 내에서 두 지점 사이에 존재하는 전파환경요소(건물, 지형, 도로 등)를 `단층 촬영과 같은 방식`으로 3차원 공간을 추출하는 알고리즘  

![image](https://user-images.githubusercontent.com/42092864/164551231-a1c72a49-983a-4e8a-aaab-c4869154d2e6.png "3D LAMS 알고리즘 예시")




## 3. PRO4S 도심지 mmWave 경로손실 웹어플리케이션 설치

 1. Fork From repository
 2. requirments.txt의 dependent library 설치
 3. SuperUser 생성 및 실행

## 4. PRO4S 도심지 mmWave 경로손실 모델 및 시각화 Flow

 1. 유저로부터 AP의 Configuration 받아온다(X,Y,Z,Downtilt,Azimuth) : 
      XYZ Coordinates as UTM EPSG:32652
      Prime meridian: Greenwich
 2. 유저의 configuration부터 서버가 예측에 필요한 자료를 생성한다.
 3.  {configuration_of_user}.xlsx, lams image of each point-point
 4. 약간의 시간(<10min)이 지난후 결과를 예측 할 수 있다.

---
본 레포지토리의 연구결과에 관심있으시다면 아래로 연락 부탁드립니다. (CINe Lab 연구 진행중, 2022-04-22 ~ )

Mail
진우빈 (ubinjin2@naver.com)
김현진 (zx8635@gmail.com)

Github
@ubinjin @ChickenRushKR
