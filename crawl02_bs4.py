# beautiful soup - 파싱 : 필요한 정보만 정제
# pip install beautifulsoup4
import bs4
html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

ul = bs_obj.find("ul")
# print(ul)
# find 함수를 이용해 원하는 요소에 접근
# text 메서드를 통해 텍스트만 출력
li = ul.find("li")
# findAll 은 해당하는 전체 요소를 리스트로 가져옴.
lis = ul.findAll("li")
# print(li.text)
print(lis)
print(lis[0])
print(lis[0].text)
