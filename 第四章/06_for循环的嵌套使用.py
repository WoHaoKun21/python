"""
    Python中for循环的嵌套使用
"""

# # 一、for循环的嵌套使用
# i = 0
# for i in range(1, 101):  # 从1到100进行循环
#     print(f"今天是向小美表白的第{i}天")
#     for j in range(1, 11):  # 每天送10多玫瑰
#         print(f"这是第{i}天送出的第{j}支玫瑰")
#     print(f"小美，我喜欢你")
# print(f"第{i}天，表白成功")

# 一、for循环的嵌套使用练习：输出9*9乘法表
for i in range(1, 10):  # 输出9行
    for j in range(1, i + 1):  # 输出行内容
        print(f"{j}*{i}={i * j}\t", end='')
    print()
