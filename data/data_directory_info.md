## Data_directory_info

[Directory 구조]

### New labeled data
#### 다시 8개로 세분화 해서 label 함

    2020_09_labeled/ 
        P1/ 
            Annotations/ 
            JPEGImages/ 
            classes.txt 
        P2/ 
            Annotations/ 
            JPEGImages/ 
            classes.txt 




### Old labeled data
#### 세포 수 변화를 모델화 하기 너무 복잡해서 5개 class로 줄이니 세분화 되지 않아 인식 오류 발생

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
   


### Old labed data
#### 8개의 class로 label한 data - 세포 수 변화를 모델화 하기 너무 복잡함

    2020_07/ 
        test/P1
        train/P1
        classes.txt
