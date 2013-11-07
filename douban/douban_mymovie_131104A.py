#encoding=utf8

__author__ = 'abc'

import urllib
import urllib2
import cookielib
from urllib import urlencode
import time

# output.html
exportFile = 'doubanMyMovie/output'

# exit(0)

###用cookielib模块创建一个对象，再用urlllib2模块创建一个cookie的handler
cookie = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

###有些网站反爬虫，这里用headers把程序伪装成浏览器
hds = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36' }

# ###登录需要提交的表单
# pstdata = {'formhash':'', #填入formhash
# 	'person[login]':'', #填入网站的用户名
# 	'person[password]':'', #填入网站密码
# 	}
#
# dt = urllib.urlencode(pstdata) #表单数据编码成url识别的格式

def get30Movie(index):
    ###登录页的url
    lgurl = 'http://movie.douban.com/people/samhooxee/collect?'
    appendDate = {
        'start': index,
        'sort': 'time',
        'rating': 'all',
        'filter': 'all',
        'mode': 'list'
    }
    enlgurl = lgurl + urlencode(appendDate)
    print enlgurl
    req = urllib2.Request(url = enlgurl,headers = hds) #伪装成浏览器，访问该页面，并POST表单数据，这里并没有实际访问，只是创建了一个有该功能的对象
    opener = urllib2.build_opener(cookie_handler) #绑定handler，创建一个自定义的opener
    response = opener.open(req)#请求网页，返回句柄
    page = response.read()#读取并返回网页内容
    return page

# print page #打印到终端显示
for i in range(1282/30+1):
    print '%s_%02d' % (exportFile, i)
    filenName = '%s_%02d' % (exportFile, i)
    with open(filenName, 'w') as f:
        print i*30
        page = get30Movie(i*30)
        f.write(page)
        time.sleep(1)
print 'done!!!'