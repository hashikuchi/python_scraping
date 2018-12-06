# coding: UTF-8
import urllib3
from bs4 import BeautifulSoup

# アクセスするURL(虚構新聞)
url = "http://kyoko-np.net/index.html"

http = urllib3.PoolManager()
response = http.request('GET', url)

soup = BeautifulSoup(response.data, "html.parser")

# トップニュースのタイトルを取得
# class='topnews' の子要素のaタグ、の子要素のh2タグ、の子要素文字列(string)を取る
print(soup.select_one('.topnews > a > h2').string)
