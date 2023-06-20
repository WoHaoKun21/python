"""
    Python包：Python异常-模块-包的综合案例
    练习案例：创建一个自定义包，名为“my_utils”
        在包内提供两个模块：
            ① str_utils.py（字符串相关工具）：
                * 函数：str_reverse(s)，接收传入字符串，将字符串进行反转返回
                * 函数：substr(s, x, y)，按照下标x和y，对字符串进行切片
            ② file_util.py（文件处理相关工具）：
                * 函数：print_file_info(file_name)，接受传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，
                      通过finally关闭文件对象
                * 函数：append_to_file(file_name, data)，接受文件路径以及传入数据，将数据追加到文件中
"""
from my_utils.str_utils import *
from my_utils.file_util import *

# 包 字符串操作
print(f"字符串acedf反转后的结果：{str_reverse('acedf')}")
print(f"字符串acedf截取后的结果：{substr('acedf', 0, 4)}")

# 包 文件操作方法
print_file_info("E:/python/9第九章：Python异常、模块与包/异常文件/异.txt")
append_to_file("E:/python/9第九章：Python异常、模块与包/异常文件/异常2.txt", "\n包添加的数据内容")
