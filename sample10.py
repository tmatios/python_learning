# より高度なスクレイピング
from bs4 import BeautifulSoup
import requests
url = 'http://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# ページ内のすべての見出しを取得
for heading in soup.find_all(['h1', 'h2', 'h3']):
    print(heading.get_text())