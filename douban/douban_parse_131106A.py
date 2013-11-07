__author__ = 'abc'

from pyquery import PyQuery as pq
import datetime

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

exportFile = 'doubanMyMovie/output'
outputFile = 'doubanMyMovie/tmp'

if __name__ == '__main__':
    MovieList = []
    for i in range(1282/30+1):
        filenName = '%s_%02d' % (exportFile, i)
        removeScript(filenName, outputFile)
        with open(outputFile) as f:
            a = f.read()
            d = pq(a)

            p = d('.item-show')
            # print len(p)
            for each in p:
                items = each.findall('div')
                OneMovie = {}
                for item in items:
                    if item.attrib['class'] == 'title':
                        href = item.find('a').attrib['href']
                        title = item.find('a').text.strip().replace(',', '_', 100)
                        OneMovie['title'] = title
                        OneMovie['href'] = href
                        pass
                    if item.attrib['class'] == 'date':
                        date = item.find('span').tail.strip()
                        OneMovie['date'] = date
                        pass
                print '%s, %s, %s' % (OneMovie['date'], OneMovie['title'], OneMovie['href'])
                MovieList.append(OneMovie)
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