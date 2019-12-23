# 특정 웹 홈페이지 크롤링


# 1. 상세 페이지 링크를 수집해 상세 페이지 크롤링
# Request 라이브러리 : http 요청을 좀더 편하게 함 (urllib에 비해)
# 라이브러리 패키지 설치시 alt + enter 를 눌러 바로 설치 가능
import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/"
result = requests.get(url=url)
bs_obj = BeautifulSoup(result.content, "html.parser")
# print(bs_obj)

# 상세 페이지 링크 뽑아내기
lf_items = bs_obj.findAll("div", {"class":"lf-item"})
# print(lf_items)
hrefs = [div.find('a')['href'] for div in lf_items]

# print(len(hrefs[0:5]))
# print(hrefs[0:5])

links = dict()
for item in lf_items:
    htitle = item.find("h4",{"class":"listing-preview-title"}).text.strip()
    aa_href = item.find("a")['href']
    links[htitle] = aa_href

# href 리스트로 받아 출력
'''
for i in hrefs:
    print(f"상세페이지 URL : {i}")
    results = requests.get(url=i)
    bs_objs = BeautifulSoup(results.content, "html.parser")
    porfile_name = bs_objs.find("div", {"class": "profile-name"})
    h1_bp_name = porfile_name.find("h1")
    bp_name = h1_bp_name.text.strip()
    print("타이틀 : ", bp_name)
    profile_content = bs_objs.find("div",{"class":"profile-cover-content"})

    location_div = profile_content.find("div", {"class": "buttons medium button-plain"})
    if location_div is not None:
        location = location_div.find("span").text.strip()
        print("위치 : ", location)

    homepage_div = profile_content.find("div", {"class": "buttons medium button-outlined"})
    if homepage_div is not None:
        homepage = homepage_div.find("a")['href'].strip()
        print("홈페이지 : ",homepage)

    print()
'''

def get_bp_info(url):
    results = requests.get(url=url)
    bs_objs = BeautifulSoup(results.content, "html.parser")
    porfile_name = bs_objs.find("div", {"class": "profile-name"})
    h1_bp_name = porfile_name.find("h1")
    bp_name = h1_bp_name.text.strip()
    print(f"{url} / {bp_name}")
    profile_content = bs_objs.find("div", {"class": "profile-cover-content"})

    dictionary1 = {}
    dictionary1['name'] = bp_name

    location_div = profile_content.find("div", {"class": "buttons medium button-plain"})
    if location_div is not None:
        location = location_div.find("span").text.strip()
        dictionary1['location'] = location
    else:
        dictionary1['location'] = ""

    homepage_div = profile_content.find("div", {"class": "buttons medium button-outlined"})
    if homepage_div is not None:
        homepage = homepage_div.find("a")['href'].strip()
        dictionary1['link'] = homepage
    else:
        dictionary1['link'] = ""

    return dictionary1

result_list = []

# 리스트 객체를 for 를 사용해서 생성시 유용
result_list = [get_bp_info(hrefs[i]) for i in range(0,5)]
# result_list = [get_bp_info(i) for i in hrefs]

print(result_list)

