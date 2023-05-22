"""
    Python：函数的参数
"""


# # 函数的参数使用：通过参数接受被计算的2个数字
# def add(x, y, z):
#     print(f"{x} + {y} + {z}的结果是：{x + y + z}")
#
#
# # 调用函数，传入被计算的2个数字
# add(5, 6, 7)

# 函数参数的练习：定义函数，接受一个参数（数字类型，表示体温），在函数体内进行体温判断（正常范围：小于等于37.5度）
def tem_check(num):
    if num <= 37.5:
        print(f"体温测量中，测量到您的体温是{num}度，体温正常，请进！")
    else:
        print(f"体温测量中，测量到您的体温是{num}度，需要隔离！")


tem_check(36.5)
tem_check(38)
