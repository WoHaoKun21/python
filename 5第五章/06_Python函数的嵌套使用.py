"""
    Python：函数的嵌套使用
        嵌套函数调用指的是一个函数里面又调用了另外一个函数
"""


# 函数的嵌套调用
def func_b():
    print(2)


def func_a():
    print(1)
    func_b()  # 函数a里面调用函数b
    print(3)


func_a()
