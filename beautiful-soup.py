import requests
from bs4 import BeautifulSoup

# 웹 페이지 가져오기
url = 'https://www.python.org/blogs/'
response = requests.get(url)

# Beautiful Soup 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')

# 웹 페이지의 최신 뉴스 제목 추출하기
news_items = soup.find_all('li', class_=False)

for item in news_items:
    print(item.text.strip())