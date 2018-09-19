import numpy as np

# array 是 numpy 的一种数据类型
# 它和 list 的区别是 array 里面所包含的元素必须相同，而 list 里面包含的元素可以不同
# [1,2,3] [1,2,3,'a']
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
], dtype=np.int)

print('number of dim:', arr.ndim)
print('shape:', arr.shape)
print('size:', arr.size)
print(arr)
print(type(arr))
print(arr.dtype)


# 生成一个全部为零的矩阵
a = np.zeros((3, 4))
print(a)