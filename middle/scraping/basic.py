from urllib.request import urlopen

html = urlopen('http://www.baidu.com').read().decode('utf-8')
print(html)