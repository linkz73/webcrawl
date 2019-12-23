import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

top_right = bs_obj.find("div", {"class":"area_links"})
first_a = top_right.find("a")
# print(first_a.text)  # 네이버를 시작으로

# 네이버 메뉴 출력하기
naver_menu = bs_obj.find("div", {"class":"area_navigation"})
menu_ul = naver_menu.find("ul", {"class":"an_l"})
menu_span = menu_ul.findAll("span", {"class":"an_txt"})
print("===== 네이버 메뉴")
for i in menu_span:
    print(i.text)

print("===== 네이버 실시간 순위")
ahlist = bs_obj.find("div", {"class":"ah_list"})
ah_li = ahlist.findAll("li", {"class":"ah_item"})
count = 0
for i in ah_li:
    count += 1
    ah_a = i.find("a", {"class": "ah_a"})
    ah_span = ah_a.find("span", {"class": "ah_k"})
    print(count, ah_span.text)


