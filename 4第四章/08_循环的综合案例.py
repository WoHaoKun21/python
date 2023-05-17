"""
   循环的综合案例：使用continue
        1、员工编号从1-20，从编号1开始，依次领取工资，没人可领取1000元
        2、领取时，财务判断员工的绩效分（1-10 随机生成），如果低于5，不发工资，换下一位
        3、如果工资发完了，结束发工资
"""
import random

money = 10000  # 公司总资金
# # 一、for循环实现
# for i in range(1, 21):  # 生成员工
#     num = random.randint(1, 10)
#     if num < 5:
#         print(f"员工{i}，绩效分{num}，不发工资，下一位")
#         continue
#     if money >= 1000:
#         money -= 1000
#         print(f"员工{i}，发放工资1000元，公司账户剩余{money}元")
#     else:
#         print(f'当前公司账户余额不足，剩余{money}元，下月再发')
#         break

# 二、while循环实现
i = 1
while i <= 20:
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i}，绩效分{num}，不发工资，下一位")
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i}，发放工资1000元，公司账户剩余{money}元")
    else:
        print(f'当前公司账户余额不足，剩余{money}元，下月再发')
        break
    i += 1
