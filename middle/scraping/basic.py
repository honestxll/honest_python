from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.baidu.com').read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
imgs = soup.find_all('img')
template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device - width
, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="ie=edge" />
  <title>Document</title>
</head>
<body>
    %s
</body>
</html>
"""
ret = open('result.html', 'w')
strTags = ''
for img in imgs:
    img['src'] = 'https:' + img['src']
    strTags += str(img) + '\n'
ret.write(template%strTags)
ret.close()
