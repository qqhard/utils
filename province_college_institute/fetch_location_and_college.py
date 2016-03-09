import urllib
import re
import os

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getProvinceAndColleges(html):
    ret = {}
    regpro = r"<div class='privence'>(.+)</div>"
    patternpro = re.compile(regpro)
    province = re.findall(patternpro,html)
    regsch = r"<div class='sperator'></div>\n<div class='schools'>([^x]+?)</div>\n</div>"
    patternsch = re.compile(regsch)
    schools = re.findall(patternsch,html)
    province_num = len(province)
    for i in range(0,province_num):
        ret[province[i]] = []
        regprosch = r'target="_blank">(.+?)</a>'
        patternprosch = re.compile(regprosch)
        proschool = re.findall(patternprosch,schools[i])
        for ps in proschool:
            ret[province[i]].append(ps)

    return ret


if __name__ == '__main__':
    url = 'http://kechenggezi.com/schools'
    html = getHtml(url)
    provinceAndCollege = getProvinceAndColleges(html)
