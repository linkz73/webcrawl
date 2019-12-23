# beautiful soup - 파싱 : 필요한 정보만 정제
# pip install beautifulsoup4
import bs4
html_str = '<html><div>hello</div></html>'
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

print(bs_obj)
# find 함수를 이용해 원하는 요소에 접근
print(bs_obj.find("div"))
print(bs_obj.find("div").text)
