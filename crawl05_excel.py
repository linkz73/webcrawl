# 국가 지표 쳬계 제공 자치단체 행정구역 및 인구현황 엑셀 파일 수정하기
# http://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1041

import openpyxl

filename = "stats.xlsx"
book = openpyxl.load_workbook(filename)

# sheet = book.worksheets[0]
sheet = book.active

data = []
for row in sheet.rows:
    data.append([
        row[0].value,
        row[9].value
    ])

del data[0]
del data[1]
del data[2]

data = sorted(data, key=lambda x:x[1])

for i, a in enumerate(data):
    if (i >= 5): break

    print(i+1, a[0], int(a[1]))

# 서울을 제외한 인구를 구하기
for i in range(0,9):
    total = int(sheet[str(chr(i + 66)) + "3"].value)
    seoul = int(sheet[str(chr(i + 66)) + "4"].value)
    output = total - seoul
    print("서울 제외 인구 : ", output)
    # 쓰기
    sheet[str(chr(i + 66)) + "21"] = output
    cell = sheet[str(chr(i + 66)) + "21"]

    # 폰트와 색상 변경
    cell.font = openpyxl.styles.Font(size=14, color="FF0000")
    cell.number_format = cell.number_format

# 엑셀파일 저장하기
filename = "population.xlsx"
book.save(filename)
print("ok")