# zip
# 返回的是一个 zip 对象，需要用 list 将结果提取成 list
a = [1, 2, 3]
b = [4, 5, 6]
c = list(zip(a, b))
print(c)

for i, j in zip(a, b):
    print(i, j)

# lambda 学过 es6 就可以容易理解了
# 以前定义函数的方法

def add(num1, num2):
    return num1 + num2

# 现在可以这样
def add2(x, y): return x + y

# 或者这样
add3 = lambda x, y: x + y

print(add3(1, 3))


# map 可以将 list 中的数据循环处理到 func 中
result = list(map(add3, [1, 2], [3, 4]))
# [1+3, 2+4]
print(result)