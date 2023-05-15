"""
    Python中while循环的基础使用
"""
# # 一、while循环的基本使用
# i = 1
# while i <= 100:
#     print("这是第%d次和小妹表白" % i)
#     if i != 100:
#         print("小美第" + str(i) + "次拒绝了你")
#     else:
#         print(f"小美在第{i}次，同意了表白")
#     i += 1

# # 二、while训练：计算1-100的和
# i = 1
# num = 0
# while i <= 100:
#     num += i
#     i += 1
# print(f"1-100的总和为：{num}")

# 三、while训练：循环猜数字案例
import random  # 引入数据库

num = random.randint(1, 100)  # 生成1-100之间的随机数
print(num)
i = 1
guess_num = int(input("请输入猜测的数字："))
while guess_num != num:
    if guess_num > num:
        print("猜测的数字偏大了")
    else:
        print("猜测的数字小了")
    guess_num = int(input("在猜一次："))
    i += 1
print(f"恭喜你在第{i}次猜对啦！！，结果是：{num}")
