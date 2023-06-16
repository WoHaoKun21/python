"""
    Python模块：模块的导入
"""
# # 模块导入的基本使用：使用import导入time模块使用sleep功能
# import time  # 导入Python内置的time模块（time.py文件），也可以写成：import time as 别名
#
# print("你好")
# time.sleep(5)  # 通过“.”就可以使用模块内部的全部功能（类、函数、变量）
# print("我也好")

# # 模块导入的基本使用：使用from导入time的sleep功能
# from time import sleep  # 在time模块中导入sleep功能
#
# print("你好")
# sleep(5)
# print("我也好")

# # 模块导入的基本使用：使用*导入time模块的全部功能
# from time import *  # “*”号表示全部功能，直接使用sleep()，不需要time.sleep()
#
# print("你好")
# sleep(5)
# print("我也好")

# # 模块导入的基本使用：使用as给模块加上别名
# import time as t
#
# print("你好")
# t.sleep(5)  # 给模块取别名，并使用其功能
# print("我也好")

# 模块导入的基本使用：使用as给定特定功能加上别名
from time import sleep as delay

print("你好")
delay(5)  # 给功能其别名，并进行正常使用
print("我也好")
