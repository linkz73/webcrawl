# 네이버 개발자센터 : 서비스 API 검색
# JSON 구조

# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import requests
import pprint
from urllib.parse import urlparse
'''
keyword = "광운대"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=100"
result = requests.get(urlparse(url).geturl(),
                      headers={"X-Naver-Client-Id": "F1drSbnhsFfyZCcGRMJE",
                               "X-Naver-Client-Secret": "GCfh6guQox"})
json_obj = result.json()
print(json_obj)
'''

def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + \
          "&display=" + str(display) + "&start=" + str(start)
    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id": "F1drSbnhsFfyZCcGRMJE",
                                   "X-Naver-Client-Secret": "GCfh6guQox"})
    return result.json()


def call_and_print(keyword, page):
    count = page
    display = 100
    json_obj = get_api_result(keyword, display, page)
    for item in json_obj['items']:
        title = str(count) + ". " + item['title'].replace('<b>', '').replace('</b>', '')
        print(title + "@" + item['bloggername'] + "@" + item['link'])
        count += 1

keyword = "광운대"
# call_and_print(keyword, 1)
# call_and_print(keyword, 101)
# call_and_print(keyword, 201)
# call_and_print(keyword, 301)
# call_and_print(keyword, 401)
#
# json_obj = get_api_result("광운대학교", 100, 101)
#
# print("total", json_obj['total'])
# print("display", json_obj['display'])
# print("start", json_obj['start'])
# print("items", len(json_obj['items']))
#
# count = json_obj['start']
# for item in json_obj['items']:
#     print(f"[{count}] title: {item['title'].replace('<b>','').replace('</b>','')}")
#     print(f"link: {item['link']}")
#     count += 1

# 엑셀 자료 나누기 : A 탭선택 - 데이터>텍스트나누기 - 구분기호로 분리됨 - 기타(@) 선택
for i in range(500):
    if i % 100 == 0:
        call_and_print(keyword, i+1)



