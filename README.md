# 2020 공개 SW 개발자대회 준비 - WYSIWYG 팀
## 개발계획서 준비중
### 이 Github는 private상태입니다. 개발 완료시점에서 public으로 전환 예정입니다. 

#### 준비사항 체크
#### 1) 개발자대회 참가서 작성(프로젝트명, 개발배경 및 목적, 개발계획)  - 작성중
#### 2) 개발 계획
    
[Labeled data acquisition process]

    1. cell 형태인식 & 자동 crop 기능 구현 --> 학습용 데이터 확보
      1-1. 세포 배양 (n=4, 각 n 당 1*10^4개 세포 seeding)
      1-2. 모든 활성단계의 세포 사진 포함; manual crop 해서 YOLO 학습용 data 확보 
            - single-cell image data (224*224 pixel) 준비 - 몇장?
      1-3. YOLO 인식 시켜서 자동 crop 기능 구현
      1-4. 확보할 data: 계대 별 500장씩 7계대 사진 확보 (총 3,500장) - 2 set확보

    2. 세포 성장상태 label을 위한 기반 data 확보: cell #, confluence 도달 시간, CFU-F data at each passage
      2-1. 각 계대 별 세포수, 계대까지 도달 시간을 기반으로 성장율 추산 CFU-F 결과와 비교해서 확인
      2-2. grade 별 PDT 값으로 label해서 성장율 예측을 위한 data로 사용
       

    3. 세포 형태에 따른 classification (3개정도는 뚜렷이 구분가능-지도학습용 data 생성) 
            -비지도학습으로 자동분류하면 인위적으로 분류한 것과 일치 할 지도 궁금한 부분임
      3-1. crop 된 data들을 Train set과 test set으로 나누어 저장  
      3-2. Train set: 
            - 500 cropped images at every passage (passage 1-7) total 3,500 cropped images
            - 전체 섞어서 세포 활성에 따른 category 로 분류 --> directory 별로 저장
            - 학습 수행
      3-3. test set: 학습 정확도 평가용 - classification test

    4. 각 세포 morphology category와 성장특성 data로 학습 running -->가중치 파일 생성
      4-1. 출력할 결과: category 별 세포 수
      4-2. 추가할 출력값: cell counting (100x 촬영사진. 시야당 cell# 파악, density 결정 point: 35% 이상만 pass)
      4-3. 출력값으로부터 계산: density 결정, 총체적 세포활성 등급 결정 
      
    5. 실제 배양사진 넣고 평가 
    
    6. Test case & bugfix
    . 
    . 
    8. Web UI 작업
    

[data 수집일정]



[구체적 코딩계획]
4) 모델의 입출력 정의
   - 세포 형태 classification - 비 지도 학습(?)
   - 다양한 세포형태 이미지 데이터와 성장특성 데이터 레이블로 학습
   - 평가용 데이터 준비 (여러 형태의 세포가 다양한 비율로 섞여있는 실제 실험 data)
   - 세포 성장율 예측의 정확성 평가 (예측 데이터와 실제 데이터 비교)
5) 질의사항(개발 요령, 코드 설계 요령 등 무엇이든)
   - 신청서 입력 사항 (프로젝트활용방향(택1): 직접 입력 - Web UI 공개를 통한 범용적 활용)
6) (필요하거나, 가능할 경우) 팀원별 역할
   - 팀장 이은아: 데이터 수집 및 레이블, 코딩(시도...???)  
   - 팀원 송미경: 코딩 및 알고리즘 구현
7) (필요하거나, 가능할 경우) Github 저장소 개설
   - 개설 완료 https://github.com/seeyourcells/ver_0.0
