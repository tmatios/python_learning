# 簡単なWebスクレイピング
import requests
from bs4 import BeautifulSoup

url = 'http://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.title.string)
