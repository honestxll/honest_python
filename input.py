# coding=utf-8
a_input = input('Please give a number:')
print(type(a_input))
print(type(1))

if a_input.isdigit():
  print('您输入的是数字')
else:
  print('您输入的不是数字')