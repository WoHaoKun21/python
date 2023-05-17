"""
    Python中for循环的基础使用
        格式：
        for 临时变量 in 待处理的数据集:
            循环满足条件时执行的代码
"""
# # 一、for循环的使用
# name = "itemName"
# for i in name:  # 将name的内容循环输出，并赋予i这个临时变量
#     print(i)

# 二、for循环训练：定义字符串name，通过for循环计算出有多少个英文字母”a“
name = "itemName is a brand of cast"
count = 0
for i in name:
    if i == "a":
        count += 1
print(f"在该字符串中，字母“a”一共出现了{count}次")
