"""
    Python的判断语句嵌套使用
        格式：
        if 条件1:
            满足条件1要做的事情
            if 条件2:
                满足条件2要做的事情
"""
# # if条件的嵌套使用
# print("欢迎来到Python课堂")
# if int(input("请输入您的身高：")) > 120:  # 如果身高大于120cm则不能进行免费，但是可以继续判断VIP等级
#     print("您的身高超出120cm，不可以免费")
#     print("如果您的VIP等级大于3，可以免费游玩")
#     if int(input("请输入您的VIP等级：")) > 3:
#         print("您的VIP等级大于3，可以免费游玩")
#     else:
#         print("对不起，您需要补票10元")
# else:
#     print("欢迎你，小朋友，可以免费游玩")

# if elif else的组合使用
# 公司发放礼物要求：1、必须是大于等于18岁小于等于30岁的成年人；2、入职时间超过两年时间，或者级别大于3才可以进行领取
age = int(input("请输入您的年龄："))
year = float(input("请输入您工作时间："))
level = int(input("请输入您的级别："))

if age >= 18:
    print("成年人符合，继续判断")
    if age <= 30:
        print("您的年龄达标，请继续判断")
        if year >= 2:
            print("您的年龄达标，工作时间超过两年，条件满足，可以领取")
        elif level > 3:
            print("您的年龄和职业级别达标，可以直接进行领取")
        else:
            print("对不起，您的年龄达标，但是您的工作年限和级别不足，不可以进行领取")
    else:
        print("您的年龄太大了，不可领取")
else:
    print("对不起，未成年不可以领取")
