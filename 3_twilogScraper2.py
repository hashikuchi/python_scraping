from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

# @hassy_nz のTwilog
url = "https://twilog.org/hassy_nz"

# Chrome バックグラウンドで実行する
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

wd = webdriver.Chrome('chromedriver', options=options)

# 1〜10ページ目までを探索する
for i in range(1, 11):
    wd.get(url + '/' + str(i))

    html = wd.page_source.encode('UTF-8')
    soup = BeautifulSoup(html, "html.parser")

    # select関数を使い、ページ内のすべてのツイートを表示する
    for tweet in soup.select('.tl-text'):
        text = ''
        for child in tweet.children:
            child = str(child)
            # HTMLタグ(<a href=''...>など)が邪魔なので削除
            child = re.sub(r'<.*>', '', child)
            text += str(child)
        print(text)
