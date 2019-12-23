# http://www.krei.re.kr:18181/new_sub01
# 농촌경제연구소 사이트의 해외곡물시장정보 를 json 으로 가져옴
# 크롬 F12 > 네트워크 > XHR > Headers --> Request URL 정보를 복사해 옴.
import xlsxwriter
from urllib.request import urlopen
import requests
import json

from_date = "2019-01-01"
to_date = "2019-12-23"
url = "http://www.krei.re.kr:18181/chart/main_chart/index/kind/C/sdate/" + \
      from_date + "/edate/" + to_date

# text = urlopen(url)
# json_objs = json.load(text)
# print(json_objs)
# for item in json_objs:
#     print(item['date'] + "@" + item['settlement'])

# json 데이터를 엑셀로 바로 저장
response = requests.get(url)
json_objs = json.loads(response.text)

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for item in json_objs:
    # worksheet.write(row, col, json.dumps(key))
    worksheet.write(row, col, int(item['date']))
    worksheet.write(row, col + 1, float(item['settlement']))
    row += 1

workbook.close()
