"""
    Python函数进阶：函数多返回值
"""


# 使用多个变量接受多个返回值
def test_return():
    return 1, "Hello", True


x, y, z = test_return()  # 变量和值对应，就会一个个接受
print(f"多个变量接受多个返回值的结果分别为：{x}-{y}-{z}")
