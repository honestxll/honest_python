# 写文件
text = 'This is my first text.\nThis is next line.'
my_file = open('myfile.txt', 'w')
my_file.write(text)
my_file.close()

# 追加文件
append_text = '\nThis is appended file 哈哈'
append = open('myfile.txt', 'a')
append.write(append_text)
append.close()

# 读取文件
file = open('myfile.txt', 'r')
content = file.read()
# content = file.readline()
# content = file.readlines()
# print(content)
# content = content.split('\n')

# 读取 list 或者是 字符串
def output(data):
  if type(data) is list:
    for txt in data:
      print(txt)
  elif type(data) is str:
    print(data)
  else:
    print('错误')

output(content)