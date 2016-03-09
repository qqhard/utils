#-*- encoding:UTF-8 -*-
import urllib2
import re
import time
import Queue
import os

def getHtml(url):
    page = urllib2.urlopen(url, timeout = 10)
    html = page.read()
    return html

def getSubjects(html):
    reg = r"<div class='subject_name'>(.+)</div>"
    subreg = re.compile(reg)
    sublist = re.findall(subreg, html)
    text = ''
    for sub in sublist:
        text += sub + '\n'
    return text

def getSchool(html):
    reg = r"<div class='sub_title'>(.+)</div>"
    schreg = re.compile(reg)
    schname = re.findall(schreg, html)[0][1:-1]
    return schname

def run(url, i):
    html = getHtml(url)
    schname = getSchool(html)
    sublist = getSubjects(html)
    os.mkdir('db')
    f = open('db/{0}-{1}.txt'.format(i, schname), 'w+')
    f.write(sublist)
    f.close()


if __name__ == '__main__':
    que = Queue.Queue(0)
    for i in range(1,2420):
        que.put(i)
    while que.empty() == False:
        i = que.get()
        url = "http://kechenggezi.com/schools/{0}/subjects".format(i)
        try:
            run(url, i)
            print '第{0}个成功'.format(i)
            time.sleep(1)
        except:
            print '第{0}个出错'.format(i)
            que.put(i)
