"""
    Python数据容器的通用操作
"""
# 数据容器的通用操作演示
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 2, 4, 3, 5}
my_dict = {"key": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# # len元素个数
# print(f"列表 元素个数有：{len(my_list)}")
# print(f"元组 元素个数有：{len(my_tuple)}")
# print(f"字符串 元素个数有：{len(my_str)}")
# print(f"集合 元素个数有：{len(my_set)}")
# print(f"字典 元素个数有：{len(my_dict)}")

# # max最大元素
# print(f"列表 最大元素为：{max(my_list)}")
# print(f"元组 最大元素为：{max(my_tuple)}")
# print(f"字符串 最大元素为：{max(my_str)}")
# print(f"集合 最大元素为：{max(my_set)}")
# print(f"字典 最大元素为：{max(my_dict)}")

# # min最小元素
# print(f"列表 最小元素为：{min(my_list)}")
# print(f"元组 最小元素为：{min(my_tuple)}")
# print(f"字符串 最小元素为：{min(my_str)}")
# print(f"集合 最小元素为：{min(my_set)}")
# print(f"字典 最小元素为：{min(my_dict)}")

# # 类型转换：容器转列表
# print(f"列表 转列表的结果是：{list(my_list)}")
# print(f"元组 转列表的结果是：{list(my_tuple)}")
# print(f"字符串 转列表的结果是：{list(my_str)}")
# print(f"集合 转列表的结果是：{list(my_set)}")
# print(f"字典 转列表的结果是：{list(my_dict)}")

# # 类型转换：容器转元组
# print(f"列表 转元组的结果是：{tuple(my_list)}")
# print(f"元组 转元组的结果是：{tuple(my_tuple)}")
# print(f"字符串 转元组的结果是：{tuple(my_str)}")
# print(f"集合 转元组的结果是：{tuple(my_set)}")
# print(f"字典 转元组的结果是：{tuple(my_dict)}")

# # 类型转换：容器转字符串
# print(f"列表 转字符串的结果是：{str(my_list)}，转换后的类型为：{type(str(my_list))}")  # 类型已经变为str类型，但是排版样式没有改变
# print(f"元组 转字符串的结果是：{str(my_tuple)}，转换后的类型为：{type(str(my_tuple))}")  # 类型已经变为str类型，但是排版样式没有改变
# print(f"字符串 转字符串的结果是：{str(my_str)}，转换后的类型为：{type(str(my_str))}")  # 类型已经变为str类型，但是排版样式没有改变
# print(f"集合 转字符串的结果是：{str(my_set)}，转换后的类型为：{type(str(my_set))}")  # 类型已经变为str类型，但是排版样式没有改变
# print(f"字典 转字符串的结果是：{str(my_dict)}，转换后的类型为：{type(str(my_dict))}")  # 类型已经变为str类型，但是排版样式没有改变

# # 类型转换：容器转集合
# print(f"列表 转集合的结果是：{set(my_list)}")
# print(f"元组 转集合的结果是：{set(my_tuple)}")
# print(f"字符串 转集合的结果是：{set(my_str)}")
# print(f"集合 转集合的结果是：{set(my_set)}")
# print(f"字典 转集合的结果是：{set(my_dict)}")

# # sorted容器排序：排序完毕后会变成列表对象
# my_list2 = [5, 6, 2, 4, 3, 1]
# my_tuple2 = (5, 6, 2, 4, 3, 1)
# my_str2 = "gecdafb"
# my_set2 = {5, 6, 2, 4, 3, 1}
# my_dict2 = {"key4": 4, "key3": 3, "key": 1, "key5": 5, "key2": 2, }
# print(f"列表容器排序结果为：{sorted(my_list2, reverse=True)}")
# print(f"元组容器排序结果为：{sorted(my_tuple2)}")
# print(f"字符串容器排序结果为：{sorted(my_str2)}")
# print(f"集合容器排序结果为：{sorted(my_set2)}")
# print(f"字典容器排序结果为：{sorted(my_dict2, reverse=False)}")  # 第二个参数表示排序后的数据时候进行反转
