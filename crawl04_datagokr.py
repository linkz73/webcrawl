# 공공데이터포털 > 데이터셋 > 오픈API
# 국내관광정보서비스 > api 선택후 > 활용신청
import requests
import bs4
# import json

endpoint = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?"
serviceKey = "colkNjJCcXW11EUqoQuhLNWmPUiskCZYJd5cSabF%2F9HRrSrFTK2lsGIi8hd%2B4ZQmH6OIEYxMBFYY5zultr5uZA%3D%3D"

numOfRows = "10"
pageSize = "1"
pageNo = "1"
MobileOS = "ETC"
MobileApp = "AppTest"
arrange = "A"
contentTypeId = "15"
areaCode = "1"
sigunguCode = "4"
listYN = "Y"

paramset = "serviceKey=" + serviceKey + "&numOfRows=" + numOfRows + "&pageSize=" + pageSize + "&pageNo=" + pageNo + \
           "&MobileOS=" + MobileOS + "&MobileApp=" + MobileApp + "&arrange=" + arrange + "&contentTypeId=" + \
           contentTypeId + "&areaCode=" + areaCode + "&sigunguCode=" + sigunguCode + "&listYN=" + listYN + "&_type=json"

url = endpoint + paramset
print(url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
print(bs_obj)