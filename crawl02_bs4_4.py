# 네이버 뉴스 가져오기
import urllib.request
import bs4

url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

print("===== 네이버 헤드라인 뉴스")
ul = bs_obj.find("ul", {"class":"type06_headline"})
li = ul.findAll("li")
# findAll : 리턴은 리스트, 결과값이 없으면 [] 반환
count = 0
for item in li:
    count += 1
    # 클래스가 없는 요소만 가져오기
    dt = item.find("dt", {"class":""})

    aa = dt.find("a")
    print(count, aa.text.strip())
    # 속성은 a href 일 경우 atag['href'] 로 가져 옴.
    print(count, aa['href'].strip())

