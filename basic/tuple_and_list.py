a_tuple = (12,3,4,5,6,9)
another_tuple = 32,4,5,6,89

a_list = [23,4,5,6,6]
a_list.remove(6)
a_list.insert(0, 1)
# 输出最后一位
print(a_list[-1])
# 输出前三位
print(a_list[0:3])
print(a_list[:3])
# 输出第三位以后的
print(a_list[3:])
# 查看列表中元素出现的次数
print(a_list.count(4))


def output(data_list):
  data_list.sort()
  for content in a_list:
    print(content)
  for index in range(len(a_list)):
    print(index, a_list[index])

output(a_list)

multi_list = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
]

# print(multi_list)