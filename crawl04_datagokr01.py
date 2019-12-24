# 공공데이터포털 > 데이터셋 > 오픈API
# 국내 약국 정보 서비스
# 미리보기 활용하는 것이 좋음
# XML 형태로 활용 예
import requests
from urllib.parse import quote
import bs4
import json
import pandas as pd

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown?"
endpoint1 = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
serviceKey = "colkNjJCcXW11EUqoQuhLNWmPUiskCZYJd5cSabF%2F9HRrSrFTK2lsGIi8hd%2B4ZQmH6OIEYxMBFYY5zultr5uZA%3D%3D"

pageNo = "1"
numOfRows = "5000"

startPage = "1"
pageSize = "10"
# 한글 인코딩을 위한 함수
Q0 = quote("서울특별시")
Q1 = quote("")
QT = "1"
QN = quote("")
QRD = "NAME"

paramset = "serviceKey=" + serviceKey + "&numOfRows=" + numOfRows + "&pageNo=" + pageNo + "&_type=json"

paramset1 = "serviceKey=" + serviceKey + "&numOfRows=" + numOfRows + "&pageSize=" + pageSize + "&pageNo=" + pageNo + \
           "&startPage=" + startPage + "&Q0=" + Q0 + "&Q1=" + Q1 + "&QT=" + QT + "&QN=" + QN + "&QRD=" + QRD + \
           "&_type=json"

paramset_xml = "serviceKey=" + serviceKey + "&numOfRows=" + numOfRows + "&pageSize=" + pageSize + "&pageNo=" + pageNo + \
           "&startPage=" + startPage + "&Q0=" + Q0 + "&Q1=" + Q1 + "&QT=" + QT + "&QN=" + QN + "&QRD=" + QRD

url = endpoint + paramset
url1 = endpoint1 + paramset1
# print(url1)
result = requests.get(endpoint1 + paramset_xml)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
# print(bs_obj)
items = bs_obj.findAll("item")
# print(items)
count = 0
for item in items:
    # print(item.find("dutyname"))
    tagged_item = item.find("dutytime1c")
    if tagged_item is not None:
        close_time = int(tagged_item.text.strip())
        if close_time > 2100:
            count += 1
            # 약국명 출력
            print(f"{count}. {item.find('dutyname').text} / {close_time}")

print("서울특별시 내 월요일 오후 9시 이후까지 하는 약국의 수 : " + str(count))
'''
response = requests.get(url1)
json_objs = json.loads(response.text)
# aa = pd.DataFrame(data=json_objs['response']['body']['items']['item'])
# print(aa)
for i in json_objs['response']['body']['items']['item']:
    print(i)
    print(i['dutyName'])
    print(i['dutyAddr'])
'''