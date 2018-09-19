import re

string = 'dog runs to cat'
pattern = 'cat'

print(pattern in string)

# 如果需要使用表达式，需要在字符串前面加一个 r
ptn = r'r[au]n'

print(re.search(ptn, string))