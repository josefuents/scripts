import codecs
import os
import re

months = ["2006/12", "2007/01", "2007/02", "2007/03", "2007/04", "2007/05", "2007/06", "2007/07", "2007/08", "2007/09", "2007/10", "2007/11", "2007/12", "2008/01", "2008/02", "2008/03", "2008/04", "2008/05", "2008/06", "2008/07", "2008/08", "2008/09", "2008/10", "2008/11", "2008/12", "2009/01", "2009/02", "2009/03", "2009/04", "2009/05", "2009/06", "2009/07", "2009/08", "2009/09", "2009/10", "2009/11", "2009/12", "2010/01", "2010/02", "2010/03", "2010/04", "2010/05", "2010/06", "2010/07", "2010/08", "2010/09", "2010/10", "2010/11", "2010/12", "2011/01", "2011/02", "2011/03", "2011/04"]

url = "iphoneblog"

def archiveUrls():
    os.mkdir('f')
    for m in months:
        os.popen("wget -O f/" + re.sub('/', '.', m) + " http://www." + url + ".de/" + m + "/")

def postsUrls():
    url_set = set()
    for fn in sorted(os.listdir("f/")):
        for line in codecs.open("f/" + fn, "r"):
            m = re.search('<a href="([^"]*)', line)
            if m != None:
                url_set.add(m.group(1))
    
    f = codecs.open('l.txt', 'w', 'utf-8')
    for u in url_set:
        print u
        f.write(u + '\n')
    f.close

#archiveUrls()
#postsUrls()
os.system('wget -x -i articles.txt')
