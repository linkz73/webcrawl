# beautiful soup - 파싱 : 필요한 정보만 정제
# pip install beautifulsoup4
import bs4
html_str = """
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

# ul = bs_obj.find("ul")
ul = bs_obj.find("ul", {"class": "greet"})

print(ul)
