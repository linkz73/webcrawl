# 네이버 개발자센터 : 서비스 API 검색

# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import requests
from urllib.parse import urlparse

keyword = "광운대"
print(keyword)
print(urlparse(keyword))