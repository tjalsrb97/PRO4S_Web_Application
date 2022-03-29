# 2021년 산학연계 프로젝트 PRO4s
-----

## 산혁연계 기업 : LG U+

## 담당 : 이혁준 교수님(CINe Lab), 이지훈 조교님

---

웹 어플리케이션을 이용하여, 아래 그림과 같이 도심지에서 mmWave전파의 경로손실을 예측할 수 있다.
> 사용된 대표적인 프레임워크/라이브러리는 Tensorflow, Mysql, Django 기반입니다!

![image](https://user-images.githubusercontent.com/42092864/120883080-278c0500-c616-11eb-8bee-07cacbc869f4.png)

###  PRO4S 도심지 mmWave 경로손실 웹어플리케이션 설치
 1. Fork From repository
 2. requirments.txt 를 확인하여 dependent 라이브러릴 설치해주세요
 3. SuperUser를 만들고 저희 웹 어플리케이션을 이용해보세요!

###  PRO4S 도심지 mmWave 경로손실 모델 및 시각화 Flow
 1. 유저로부터 AP의 Configuration 받아온다(X,Y,Z,Downtilt,Azimuth) : 
      XYZ Coordinates as UTM EPSG:32652
      Prime meridian: Greenwich
 2. 유저의 configuration부터 서버가 예측에 필요한 자료를 생성한다.
 3.  {configuration_of_user}.xlsx, lams image of each point-point
 4. 약간의 시간(<10min)이 지난후 결과를 예측 할 수 있다.
