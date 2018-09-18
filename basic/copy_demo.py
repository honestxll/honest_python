# 文件名不能和模块名一样
import copy

a = [1, 2, [1, 2]]
b = a
b[0] = 11

print(id(a) == id(b))

c = copy.copy(a)

print(id(a) == id(c))
print(id(a[2]) == id(c[2]))

d = copy.deepcopy(a)
print(id(a[2]) == id(d[2]))