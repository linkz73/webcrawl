import csv, codecs

# CSV 파일 저장
'''
with codecs.open("test.csv", "w", "euc_kr") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["ID", "이름", "가격"])
    writer.writerow(["1000", "SD 카드", 30000])
    writer.writerow(["1001", "키보드", 10000])
    writer.writerow(["1002", "마우스", 20000])
    writer.writerow(["1003", "그래픽", 130000])
'''

# CSV 파일 열기
filename = "test.csv"
fp = codecs.open(filename, "r", "euc_kr")

# 한줄씩 읽어 들이기
reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader:
    print(cells[0], cells[1], cells[2])
