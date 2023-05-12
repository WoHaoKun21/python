"""
    Python的 if elif else组和用法
    格式：
        if 要判断的条件:
            条件成立时要做的事情
        else:
            条件不成立要做的事情
"""

# # 一、if elif else的组合使用
# height = int(input("请输入您的身高（cm）："))
# vip_level = int(input("请输入您的VIP等级（1~5）："))
# if height < 120:
#     print("您的身高小于120，可以免费游玩")
# elif vip_level > 3:
#     print("您的VIP等级大于3，也可以免费游玩")
# else:
#     print("对不起，您各项条件都不满足，需补票10元")
# print("祝您游玩愉快")

# # 二、if elif else的组合使用
# height = int(input("请输入您的身高（cm）："))
# vip_level = int(input("请输入您的VIP等级（1~5）："))
# day = int(input("请告诉我今天是几号："))
# if height < 120:
#     print("您的身高小于120，可以免费游玩")
# elif vip_level > 3:
#     print("您的VIP等级大于3，也可以免费游玩")
# elif day == 1:
#     print("今天是1好免费日，您可以免费游玩")
# else:
#     print("对不起，您各项条件都不满足，需补票10元")
# print("祝您游玩愉快")

# # 三、if elif else的组合使用
# if int(input("请输入您的身高（cm）：")) < 120:
#     print("您的身高小于120，可以免费游玩")
# elif int(input("请输入您的VIP等级（1~5）：")) > 3:
#     print("您的VIP等级大于3，也可以免费游玩")
# elif int(input("请告诉我今天是几号：")) == 1:
#     print("今天是1好免费日，您可以免费游玩")
# else:
#     print("对不起，您各项条件都不满足，需补票10元")
# print("祝您游玩愉快")

# 四、if elif else的练习：猜一猜心里想的数字
num = 10
if int(input("请输入第一次猜想的数字：")) == num:
    print(f"厉害啊，第一次就猜对了，结果为：{num}")
elif int(input("不对，再猜一次：")) == num:
    print(f"恭喜你，猜对了，结果为：{num}")
elif int(input("不对，最后再猜一次：")) == num:
    print(f"恭喜你，猜对了，结果为：{num}")
else:
    print(f"很抱歉，猜错次数超出，答案为{num}")
