# coding: UTF-8
import urllib3
from bs4 import BeautifulSoup

# アクセスするURL(虚構新聞)
url = "http://kyoko-np.net/index.html"

http = urllib3.PoolManager()  # コネクションプールを開く
response = http.request('GET', url)  # HTTPリクエストを発行

# プログラミングで扱いやすい形に変形
soup = BeautifulSoup(response.data, "html.parser")

# トップニュースのタイトルを取得
# class='topnews' の子要素のaタグ、の子要素のh2タグ、の子要素文字列(string)を取る
target = soup.select_one('.topnews > a > h2')
print(soup.select_one('.topnews > a > h2').string)

# get() 関数を使うとHTMLタグのアトリビュート（属性）も取れる
link = soup.select_one('.topnews > a')
print(link.get('href'))
