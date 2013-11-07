__author__ = 'abc'

import HTMLParser
from pyquery import PyQuery as pq
# from lxml import etree
import datetime

class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'li':
            try:
                for name,value in attrs:
                    # if name == 'href':
                    print value
            except:
                print 'error onece'


def removeScript(input, output):
    with open(input) as f1:
        with open(output, 'w') as f2:
            scriptFlag = 0
            for eachline in f1:
                tagStartCnt = eachline.count('<script')
                tagStopCnt = eachline.count('/script>')
                if tagStartCnt == tagStopCnt+1 :
                    if scriptFlag == 0:
                        scriptFlag = 1
                        # print eachline
                    else:
                        print '----------------' + eachline
                elif tagStartCnt+1 == tagStopCnt :
                    if scriptFlag == 1:
                        scriptFlag = 0
                        # print eachline
                    else:
                        print '----------------' + eachline
                elif tagStartCnt == tagStopCnt and tagStartCnt != 0:
                    # print eachline
                    pass
                else:
                    if scriptFlag==0:
                        f2.write(eachline)

def printValue(v, x):
    print v
    print type(x)
    print x.text

exportFile = 'doubanMyMovie/output'
outputFile = 'doubanMyMovie/tmp'

if __name__ == '__main__':
    MovieList = []
    for i in range(1282/30+1):
        filenName = '%s_%02d' % (exportFile, i)
        removeScript(filenName, outputFile)
        # with open('outputNoscript.html') as f:
        #     a = f.read()
        # my = MyParser()
        # my.feed(a)
        with open(outputFile) as f:
            a = f.read()
            # d = pq(filename='outputNoscript.html')
            d = pq(a)

            p = d('.item-show')
            # print len(p)
            # p.each(printValue)
            # p.each(lambda e: e('.title a').text())
            for each in p:
                items = each.findall('div')
                OneMovie = {}
                for item in items:
                    # print type(item)
                    # print item.attrib
                    if item.attrib['class'] == 'title':
                        href = item.find('a').attrib['href']
                        title = item.find('a').text.strip().replace(',', '_', 100)
                        OneMovie['title'] = title
                        OneMovie['href'] = href
                        pass
                    # still problem
                    if item.attrib['class'] == 'date':
                        date = item.find('span').tail.strip()
                        OneMovie['date'] = date
                        # print item.text.strip()
                        pass
                # print '%s, %s, %s' % (OneMovie['date'], OneMovie['title'], OneMovie['href'])
                MovieList.append(OneMovie)

            # titles = d('.item-show .title a')
            # dates = d('.item-show .date')
            # for each in titles:
            #     print each.text.strip()
            # for each in dates:
            #     print each.text

            # print titles.text()
            # print len(titles)
            # print dates.text()
            # print len(dates)
    cnt2010 = {}
    cnt2011 = {}
    cnt2012 = {}
    cnt2013 = {}
    for i in range(365+1):
        cnt2010[i] = 0
        cnt2011[i] = 0
        cnt2012[i] = 0
        cnt2013[i] = 0
    for each in MovieList:
        y,m,d = each['date'].split('-')
        d1 = datetime.date(int(y),int(m),int(d)).timetuple()
        if d1.tm_year == 2010:
            cnt2010[d1.tm_yday] += 1
            # print '%d, %d, %s, %s, %s' % (d1.tm_yday, cnt2010[d1.tm_yday], y, m, d)
        if d1.tm_year == 2011:
            cnt2011[d1.tm_yday] += 1
        if d1.tm_year == 2012:
            cnt2012[d1.tm_yday] += 1
        if d1.tm_year == 2013:
            cnt2013[d1.tm_yday] += 1
    print '-----------------------------------------'
    for i in range(365+1):
        print cnt2010[i]