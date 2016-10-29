#!/usr/bin/env python  
#encoding:utf-8  
'''''getHexunGold.py 获取和讯网最新的黄金价格信息（人民币／克）'''  
  
from urllib import urlretrieve  
from time import sleep  
from time import ctime  
  
def getHexunGoldPrice(webpage):  
    f = open(webpage)  
    lines = f.readlines()  
    for eachLine in lines:  
        if '<p class="date">' in eachLine:  
            print ctime(), ' ------- ', 
            eachLine.strip()[eachLine.strip().index('>') + 1 : eachLine.strip().rindex('<')], 
            '人民币／克'  
            break  
    f.close()  
  
def download(url='https://cjb.alipay.com/gold/guide.htm;jsessionid=72ADD6AFEED20C654D2FF2A2D0E11CA9', process=getHexunGoldPrice):  
    try:  
        retval = urlretrieve(url)[0]  
    except IOError:  
        retval = None  
  
    if retval:  
        process(retval)  
  
if __name__ == '__main__':  
    while True:  
        #print 'a'  
        download()  
        sleep(2)  