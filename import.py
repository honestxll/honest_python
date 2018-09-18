import time
import module.m1 as m1
# 自己写的模块需要在那个模块里面放一个空的 __init__.py 文件
# from time import localtime, time
# from time imoprt *
# import time as t

m1.output(time.localtime().tm_year)
