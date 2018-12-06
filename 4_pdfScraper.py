from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open


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

# 適宜整形してやる必要はある……
print(outputString)
pdfFile.close()
