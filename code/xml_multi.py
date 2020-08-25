# Cell_P1 레이블링 한 파일의 class별 개수 확인
# xml_cell_p1.csv 파일에 xml 파싱한 결과 저장

import xml.etree.ElementTree as ET
import csv
import os


f = open('xml_cell_p1.csv', 'w')
csvwriter = csv.writer(f)

count = 0

head = ['File Name','Object Name']
csvwriter.writerow(head)


for file in os.listdir("./xml_files"):
    file_path = os.path.join("./xml_files", file)
    tree = ET.parse(file_path)
    root = tree.getroot()

    if (os.path.isfile(file_path)):
        for object in root.findall('object'):
            row = []
            file_name = file_path
            row.append(file_name)
            object_name = object.find('name').text
            row.append(object_name)
            csvwriter.writerow(row)
f.close()