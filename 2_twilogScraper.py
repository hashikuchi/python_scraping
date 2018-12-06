# coding: UTF-8
import urllib3
from bs4 import BeautifulSoup

# @hassy_nz のTwilog
url = "https://twilog.org/hassy_nz"

http = urllib3.PoolManager()
response = http.request('GET', url)

soup = BeautifulSoup(response.data, "html.parser")

# 最新のツイート1件を取得したい
print(soup.select_one('.tl-text').string)
