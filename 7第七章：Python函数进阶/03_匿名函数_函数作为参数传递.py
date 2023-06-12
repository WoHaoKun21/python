"""
    Python函数进阶：匿名函数——函数作为参数进行传递
"""


# 函数作为参数的传递使用
def test_func(callback):
    result = callback(1, 2)
    print(f"callback参数的类型是：{type(callback)}")
    print(result, type(callback))


def compute(x, y):
    return x + y


test_func(compute)  # 将函数当作参数进行传递
