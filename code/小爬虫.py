import urllib.request
url='https://www.jinpiaotong.com/'
webPage=urllib.request.urlopen(url)
data=webPage.read()
data=data.decode('gb2312')
print(data)
#print(type(webPage))
#print(webPage.geturl())
print(webPage.info())
#print(webPage.getcode())