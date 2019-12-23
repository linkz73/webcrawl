# json 구조
json = {"name": "홍길동",
        "age": "32",
        "where": "서울시",
        "phone": "010-1234-5678",
        "friends": [
            {"name": "김갑수", "age":"33"},
            {"name": "홍홍기", "age":"35"},
        ]
       }

print(json.keys())
print(json.values())
print(json.items())

friends = json['friends']
for friend in friends:
    print(friend['name'], friend['age'])


# json 뷰어 사용하기
# http://jsonviewer.stack.hu/
# Text 탭에 붙여 넣고, Viewer 탭에서 볼 수 있음
   
