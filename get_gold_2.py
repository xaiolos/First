#!/usr/bin/env python  
#coding=utf-8
__author__ = 'Daemon'

import urllib2,re,time

class CB_Spider:
    def __init__(self):
        self.page=1
        self.enable=True

#正则获取段子内容
def getPageContent(self):
    myUrl='http://www.qiushibaike.com/hot/page/'+str(self.page)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(myUrl, headers = headers)  #模拟浏览器
    myResponse=urllib2.urlopen(req)
    myPgae=myResponse.read()
    unicodePage=myPgae.decode('utf-8')
    #根据正则表达式拿到所有的内容
    myItems=re.findall('<div.*?class="content">(.*?)</div>',unicodePage,re.S)
    items=[]

    print u'第%s页数据展示 ' %self.page

    for item in myItems:
        content=item.strip()
        #拿到最后的<!--12345678910-->时间戳
        timeContent=re.findall(r'<!--(.*?)-->',content)
        #去掉时间戳
        pattern=re.compile(r'<!--(.*?)-->')
        content=re.sub(pattern,'',content)
        if len(timeContent)>0:
            timeContent=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(timeContent[0])))
        else:
            timeContent=''
        #每个段子前加上发布时间
        print timeContent +'\n'+content

    self.page+=1;

print u'''

-----------------------------
操作:输入daemon退出
功能:按下回车依次浏览今日的糗百热点
-----------------------------

'''

cbSpider=CB_Spider()
while cbSpider.enable:
    myInput=raw_input()
    if 'daemon'==myInput:
        cbSpider.enable=False
    #break
    else:
        getPageContent(cbSpider)