# Data_directory_info


## 2020_10 Labeled data 
### Cell type: MSC (성체 유래 세포)
### Label 내용
#### * 성체 유래 줄기세포라서 세포 형태가 보다 안정화 되어 있음
#### * 4개의 Class로 label (polygonal, small-round, spread, Etc)
#### * 세포 type에 따른 인식 정확도를 높이기 위한 추가결과

        P1/ 
            Annotations/ 
            JPEGImages/ 
            classes.txt 

        P2/ 
            Annotations/ 
            JPEGImages/ 
            classes.txt 


## 2020_09 Labeled data
### Cell type: MSC (미성숙 개체 유래)
### Label 내용
#### * 다시 8개로 세분화 해서 label 
#### * 세포 형태에 따른 성장 kinetics 모델과 맞추는 과정에서 3개의 class로 label들을 통합하는 규칙을 정해서 세포 형태 별 population의 변화를 lab data와 비교 분석 수행

    2020_09_labeled/ 
        P1/ 
            Annotations/ 
            JPEGImages/ 
            classes.txt 
        P2/ 
            Annotations/ 
            JPEGImages/ 
            classes.txt 
        P3/ 
            Annotations/ 
            JPEGImages/ 
            classes.txt 




## Old labeled data (2020년 8월)
### Cell type: MSC (미성숙 개체 유래)
### Label 내용
#### * 세포 수 변화를 모델화 하기 위해 5개 class로 줄이니 인식 오류 발생

    2020_08_labeled/ 
        P1/ # 총 388개 파일 (194개 이미지 *.jpg 파일과 *.xml 파일 같이 들어있음)
            Annotations/
            JPEGImages/
            classes.txt
        P2/ # 총 396개 파일 (198개 이미지)
            Annotations/
            JPEGImages/
            classes.txt
        P3/ # 총 284개 파일 (142개 이미지)
            Annotations/
            JPEGImages/
            classes.txt
        P4/ # 총 162개 파일 ( 81개 이미지)
            Annotations/
            JPEGImages/
            classes.txt
        P5/ # 총 238개 파일 (119개 이미지)
            Annotations/
            JPEGImages/
            classes.txt
        P6/ # 총 238개 파일 (119개 이미지)
            Annotations/
            JPEGImages/
            classes.txt
   


## Old labed data (2020년 7월)
### Cell type: MSC (미성숙 개체 유래)
### Label 내용
#### * 미성숙 개체유래 세포라서 다양한 세포 형태가 관찰됨
#### * 8개의 class로 세분화 하여 label함
#### * (예상되는 난점) 세포 수 변화를 모델화 하기 너무 복잡함

    2020_07/ 
        test/P1
        train/P1
        classes.txt
