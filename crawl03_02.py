# 웹쇼핑몰 크롤링 작업
# 쇼핑몰 데이터 수집해 크롤링 자동화

# 대상 사이트 jolse
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0'}
url = "http://jolse.com/category/toners-mists/1019/"
result = requests.get(url=url, headers=headers)
bs_obj = BeautifulSoup(result.text, "html.parser")

# 페이지네이션 링크 뽑아내기
pagination = bs_obj.find("div",{"class":"df-base-paging"})
next_link = pagination.findAll("p")[2].find("a")['href']

link_list = []
li_item = pagination.find("li")
link_list.append(url + li_item.find('a')['href'])
link_list.append(url + next_link)

while next_link != "#none":
    url1 = url + next_link
    result1 = requests.get(url=url1, headers=headers)
    bs_obj1 = BeautifulSoup(result1.text, "html.parser")
    pagination = bs_obj1.find("div", {"class": "df-base-paging"})
    next_link = pagination.findAll("p")[2].find("a")['href']
    if next_link != "#none":
        link_list.append(url + next_link)

# print(link_list)
result_list = []

def get_product_info(url):
    global result_list
    print(url)
    results = requests.get(url=url, headers=headers)
    bs_obj = BeautifulSoup(results.text, "html.parser")

    li_items = bs_obj.findAll("li", {"class": "item xans-record-"})
    dictionary1 = {}
    for item in li_items:
        pname = item.find("p", {"class", "name"})
        name = pname.find("span").text.strip()
        dictionary1['name'] = name
        ulitem = item.find("ul", {"class", "xans-product-listitem"})
        liitem = ulitem.find("li", {"class", "xans-record-"})
        price = liitem.findAll("span")[1].text.strip()
        dictionary1['price'] = price
        alink_wrap = item.find("div", {"class", "thumbnail"})
        alink = alink_wrap.find("a")['href']
        dictionary1['link'] = url + alink
        result_list.append(dictionary1)

    # return {"name":name, "price":price, "link":link}

for i in link_list:
    get_product_info(i)

print(result_list)
print(len(result_list))
