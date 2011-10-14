import codecs

f = codecs.open('l.txt', 'r', 'utf-8')
url_list = codecs.open('articles.txt', 'w', 'utf-8')

count = 0

for l in f:
    print l[19:-20]
    if l[-1] == ' ' or '':
        pass
    else:
        url_list. write('http://www.fr.wikipedia.org/wiki/' + l[19:-20] + '?action=render' + '\n')
  


