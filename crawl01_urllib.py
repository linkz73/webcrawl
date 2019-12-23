from urllib.request import urlopen

# url 주소를 가져 옴
url = "http://www.naver.com"
html = urlopen(url)

print(html.read())

# urllib : 전체 데이터를 url 로부터 가져오기




