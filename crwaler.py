from bs4 import BeautifulSoup
import requests

lotto_service_url = 'https://dhlottery.co.kr/common.do?method=main'
html = requests.get(lotto_service_url).text;
soup = BeautifulSoup(html, 'html')
print(soup)
