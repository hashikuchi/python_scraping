# coding: UTF-8
import urllib3
from bs4 import BeautifulSoup

# 【ミニワークショップ】
# 次のブログにある、すべての記事タイトルを取得し、title.txtというファイルに書き込んでみよう！
url = "http://www.moyacinema.com"
textFile = open("titles.txt", "w")

with textFile:
    while True:
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        soup = BeautifulSoup(response.data, "html.parser")

        # TODO ページ中の記事タイトルをすべて取得してtargetsに代入してください
        targets = soup.select('.entry-title-link')
        for target in targets:
            textFile.write(target.string + '\n')

        # TODO 「次のページ」の要素を取得してnextLinkに代入してください
        nextLink = soup.select_one('.pager-next > a')
        if(nextLink == None):
            break

        # TODO 「次のページ」に行くためのリンク（href要素）をnextLinkから取得してurlに代入してください
        url = nextLink.get('href')
