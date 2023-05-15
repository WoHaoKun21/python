"""
    Python中while循环的嵌套使用
        格式：
        while 条件1:
            条件1满足时，做的事情1
            条件1满足时，做的事情1
            ...（省略）...
            while 条件2:
                条件2满足时，做的事情1
                条件2满足时，做的事情1
                ...（省略）...
"""
# # 一、while循环的嵌套使用
# i = 1
# while i <= 100:
#     print(f"今天是第{i}天，我准备表白...")
#     j = 1
#     while j <= 10:
#         print(f"今天送给小美的第{j}支玫瑰")
#         j += 1
#     print("小美，我喜欢你")
#     i += 1
# print(f"坚持到第{i - 1}天，表白成功")

# 二、while循环嵌套训练：9*9乘法口诀——print()方法实现不换行
# print('hello1', end='')  # end：实现print()方法之间不换行
# print("Hello\tWord")  # \t：可以实现键盘上的Tab空格；
i = 1
while i <= 9:  # 这个外层while循环生成行：一共9行
    j = 1
    while j <= i:  # 这个内层while循环，生成内容
        print(f"{j}*{i}={i * j}\t", end='')  # 内容print语句不换行
        j += 1
    i += 1
    if i != 10:
        print()  # 实现换行效果
