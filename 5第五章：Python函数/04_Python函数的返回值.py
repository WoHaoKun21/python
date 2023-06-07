"""
    Python：函数的返回值
        Python中有一个特殊的字面量：None，其类型是：<class 'NoneType'>
        当函数没有返回值的时候，实际上就是返回了None这个字面量
"""

# # 一、函数返回值的使用
# def add(x, y):
#     return x + y
#     # # return之后的代码输出
#     # print("return之后的输出")
#
#
# r = add(2, 5)
# print(f"2 + 5的结果为：{r}")

# # 二、函数返回值的None类型，<class 'NoneType'>
# def none_check(x):
#     print(x)
#
#
# result = none_check(5)
# print(f"无返回值函数，返回的内容是： {result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")
#
#
# # 三、函数主动返回None类型
# def none_check2(x):
#     print(x)
#     return None
#
#
# result = none_check2(5)
# print(f"返回的内容是： {result}")
# print(f"返回的内容类型是：{type(result)}")


# # 三、在if中使用None类型
# def check_age(age):
#     if age >= 18:
#         return "SUCCESS"
#     else:
#         return None
#
#
# result = check_age(16)
# if not result:  # not：相当于取反，如果result为None取反后就为True
#     print("未成年，不可以进入")

# 四、None用于声明无初始内容的变量
name = None  # None字面量可以赋予变量
