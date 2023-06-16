"""
    Python模块：模块的自定义
        使用“自定义包”文件夹下面的my_module1.py文件
"""
# # 一、引入自定义包
# import my_module1
# from my_module1 import add
#
# print("模块计算两数之和为：", my_module1.add(1, 2))
# print("方法计算两数之和为：", add(5, 8))

# # 二、当两个模块方法一样的情况会使用那个模块
# from my_module1 import add
# from my_module2 import add
#
# print("方法计算两数之和为：", add(5, 8))  # 使用了模块二的功能

# # 三、当模块里的功能调用测试，我们导入后会怎么样，该怎么解决：__main__变量
# from my_module1 import add  # 解决方法在模块里面

# 四、__all__变量
from my_module1 import *  # 当引用__all__变量之后，只有这种导入方法无法使用某些功能

add(1, 2)
sub(3, 2)
