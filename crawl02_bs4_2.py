# beautiful soup - 파싱 : 필요한 정보만 정제
# pip install beautifulsoup4
# 속성별 접근 방법
import bs4
html_str = """
<html>
    <body>
        <ul class="ko">
            <li>
                <a href="https://www.naver.com">네이버</a>
            </li>            
        </ul>
        <ul class="sns">
            <li>
                <a href="https://www.facebook.com">페이스북</a>
            </li>            
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

atag = bs_obj.find("a")
print(atag)

# 속성 출력
print(atag['href'])