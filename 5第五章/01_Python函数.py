"""
    Python：python函数---是组织好的，可以重复使用的，用来实现特定功能的代码段
        不使用python内置函数len()完成字符串长度计算
"""
# 不使用python内置函数len()完成字符串长度计算
str1 = "length"
str2 = "itemName"
str3 = "QDYJZRQ"


# 不适用内置函数len()，统计出字符串长度

# # 方法一：通过for循环进行长度计量——代码量大
# count = 0
# for i in str1:
#     count += 1
# print(f"str1字符串的长度为{count}")
#
# count = 0
# for j in str2:
#     count += 1
# print(f"str2字符串的长度为{count}")
#
# count = 0
# for k in str3:
#     count += 1
# print(f"str3字符串的长度为{count}")

# 方法二：封装函数用来优化方法一
def my_len(data):  # 使用def来定义一个my_len函数
    count = 0
    for i in data:
        count += 1
    print(f"字符串长度为：{count}")


my_len(str1)
my_len(str2)
my_len(str3)
