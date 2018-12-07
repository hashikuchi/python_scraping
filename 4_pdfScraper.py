from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import csv


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content


# 大阪市の推計人口
pdfFile = urlopen(
    'http://www.city.osaka.lg.jp/hodoshiryo/cmsfiles/contents/0000392/392906/H29-3-suikei.pdf')
outputString = readPDF(pdfFile)
print(outputString)


def filterEmptyValue(word):
    return word != ''


words = outputString.split('\n')
words = list(filter(filterEmptyValue, words))  # 空の行を削除

# CSVに整形する
end = words.index("（単位：人）")
data = [["区名", "総数", "男", "女", "面積", "人口密度", "世帯数", "世帯数増減", "前月人口"]]

# データを9行ずつ取得してグルーピング
for i in range(8, end, 9):
    tempData = []
    for j in range(0, 9):
        tempData.append(words[i + j])
    data.append(tempData)

pdfFile.close()

# CSVに書き込む
csvFile = open("osaka.csv", "w")
with csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(data)
