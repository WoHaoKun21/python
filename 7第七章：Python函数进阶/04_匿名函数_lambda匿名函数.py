"""
    Python函数进阶：匿名函数——lambda匿名函数
"""


# 匿名函数的使用
def test_func(callback):
    result = callback(1, 2)
    print(f"结果为：{result}")


test_func(lambda x, y: x + y)  # 定义匿名函数，并当作参数进行传递，函数体只支持一行代码
