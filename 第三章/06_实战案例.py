"""
    Python的实战案例：数字猜测判断
"""
# 实战案例
# 1、构建随机的数字变量
import random

num = random.randint(1, 10)
print(num)

guess_num = int(input("你要猜测的数字："))

# 通过if判断语句进行数字判断
if guess_num == num:
    print("恭喜您，第一次就猜测成功")
else:
    if guess_num > num:
        print("您输入的数字大了")
    else:
        print('您输入的数字小了')
    guess_num = int(input("请再次输入你要猜测的数字："))
    if guess_num == num:
        print("恭喜您，第二次就猜测成功")
    else:
        if guess_num > num:
            print("您输入的数字大了")
        else:
            print('您输入的数字小了')
        guess_num = int(input("您还有最后一次猜测的机会："))
        if guess_num == num:
            print("恭喜您，第三次就猜测成功")
        else:
            print("很遗憾，您三次都没有猜对")
