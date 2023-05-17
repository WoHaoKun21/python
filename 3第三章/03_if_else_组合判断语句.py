"""
    Python的 if else组和用法
    格式：
        if 要判断的条件:
            条件成立时要做的事情
        else:
            条件不成立要做的事情
"""

# # if else的使用
# age = int(input("请输入您的年龄："))
# if age >= 18:
#     print("您已成年，游玩需要补票10元")
# else:
#     print("您未成年，可以免费游玩")
# print("祝您游玩愉快")

# if else的练习
height = int(input("请输入您的身高（cm）："))
if height > 120:
    print("您的身高超出120cm，游玩需要补票10元")
else:
    print("您的身高未超出120cm，可以免费游玩")
print("祝您游玩愉快")
