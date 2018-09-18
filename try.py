# 处理了错误不会影响后面代码的执行
name = 'honest'
try:
  print(name)
except Exception as error:
  print(error)
else:
  # 如果 try 里面执行成功，就会到 else 里面，表示没有获取到错误
  print('name is ok')

print('done')