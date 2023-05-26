"""
    Python的数据容器：tuple（元组）的操作
        ① index(元素)：查找某个数据，如果数据存在则返回数据对应下标，否则报错
        ① count(元素)：统计某个数据在当前元组出现的次数
        ① len(元组)：统计元组内的元素个数
"""
tuple_list = (2, 6, 3, False, 6, 3, 10)
# # 一、index()
# num = tuple_list.index(10)
# print(f"10在元组中的下标：{num}")

# # 二、count()
# count = tuple_list.count(6)
# print(f"6在元组中出现的次数：{count}")

# # 三、len()
# length = len(tuple_list)
# print(f"tuple_list的元组内容长度：{length}")

# # 元组的遍历：while循环
# i = 0
# while i < len(tuple_list):
#     print(f"while循环遍历到的元组元素：{tuple_list[i]}")
#     i += 1

# 元组的循环：for循环
for element in tuple_list:
    print(f"for循环遍历到的元组元素：{element}")
