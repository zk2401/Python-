import urllib.request
import socket
import re
import sys
import os
#targetDir='C:\Users\zk\Desktop\python学习\downloadPic'
targetDir= r'c:\Users\zk\Desktop\python学习\downloadPic'
def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos=path.rindex('/')
    t=os.path.join(targetDir,path[pos+1:])
    return t
if __name__=='__main__':
    weburl='http://www.douban.com/'
    webheaders={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req=urllib.request.Request(url=weburl,headers=webheaders)
    webpage=urllib.request.urlopen(req)
    contentBytes=webpage.read().decode('UTF-8')
    #print(contentBytes)
    setlink=set(re.findall(r'(https:[^s]*?(jpg|png|gif))',str(contentBytes)))
    print(setlink)
    for link,t in setlink:
        print(link)
        try:
            print(destFile(link))
            urllib.request.urlretrieve(link,destFile(link))
        except:
            print('下载失败')
