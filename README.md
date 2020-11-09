﻿# 프로젝트명: See_your_cells

## 개발 개요 - 2020 공개 SW 개발자대회 참가 출품작(팀명: WYSIWYG) 

### 개발배경
    
중배엽성 줄기세포는 체외배양 과정에서 점차로 활성을 잃어버리고 노화가 일어나, 활용이 어려워지는 상태에 도달하게 됩니다. 또한 노화 외에도, 줄기세포 공여자에 따른 개인차가 반영되어 증식 특성과 세포 노화의 시기가 일정하지 않게 나타날 수 있어서 배양과정에서 주의 깊게 관찰할 필요가 있습니다. 
배양과정에서 나타나는 활성의 변화를 확실하게 검증하기 위해 세포의 활성을 명확하게 측정하는 실험적 방법들이 있으나 대부분 세포를 파괴하여 측정하는 방법들이라 배양 중인 세포를 소모하게 됩니다. 


### 개발목적

세포의 노화 과정에서 미묘하게 나타나는 형태적 변화와 세포 성장의 관련성을 실험결과로 검증하고 이러한 형태 변화를 줄기세포 배양 전문가가 상주하며 모니터링 하지 않아도 판별할 수 있도록 머신러닝으로 학습시켜 세포의 배양 상태 모니터링을 자동화할 수 있는 기술을 개발하고자 합니다. 


### 진행 과정
    
[Labeled data acquisition process]

    1. 실험실에서 배양한 줄기세포의 노화 단계 별 세포 이미지 획득
      1-1. 토끼 유래 중배엽성 줄기세포 배양 (n=4)
      1-2. labelImg를 이용한 데이터 레이블: YOLO 학습용 data 확보 
      1-3. 확보한 data 수: 100배율 이미지 497장 (장 당 세포사진 3~10개) 
      1-4. 데이터 상태에 맞춘 YOLO 학습 최적 조건 탐색 

    2. 세포 활성/노화 상태 확인을 위한 기반 data 확보: 계대 별 cell #, confluence 도달 시간, 콜로니 형성능
      2-1. 각 계대 별 세포수 기반으로 성장율 추산 후 CFU-F 결과와 비교해서 활성 정도 비교
      2-2. 계대 별 population doubling time을 반영하여 성장율 예측을 위한 data로 사용


[Web UI design]

    3. Web UI Design 통해 입력된 세포 이미지를 인식하여 성장율을 예측하고 계대 시점 예측
      3-1. 입력받을 결과: 세포 이미지 (촬영 배율 100x 한정), Species, 세포 type, 계대 수
      3-2. 출력할 결과: 예측 계대 시점, 세포 활성도 예측, 총체적 세포활성 등급 결정 
    
    4. Web UI 작업
      4-1. Test run: 입력된 세포 이미지를 인식하여 성장율와 세포활성도 및 계대 시점 예측치 출력
    
    5. Test case & bugfix


[모델]   
    * 모델의 입출력 정의   
      - 세포 형태 classification - label data를 이용한 지도학습   
      - 다양한 세포형태 판독 레이블 데이터로 학습   
      - 평가용 데이터 준비 (여러 형태의 세포가 다양한 비율로 섞여있는 실제 실험 data)   
      - 세포 성장율 예측의 정확성 평가 (예측 데이터와 실제 데이터 비교)   

[팀원별 역할]   
     - 팀장 이은아: 데이터 수집, 레이블, 세포 상태 분석실험   
     - 팀원 송미경: 코딩 및 알고리즘 구현   



## Web UI 기반 SW 공개 마일스톤   
   
[Github 저장소 개설]   
    - 개설 완료 https://github.com/seeyourcells/seeyourcells

[Web page 링크]   
    - 경희대학교 TERM lab 웹 페이지: term.khu.ac.kr [term.khu.ac.kr]



