"""
    Python数据容器，set集合
        特点：不支持元素重复（自带去重功能），并且内容是无序的。而数据容器都是有序切可以支持重复元素，具有局限性
"""
# # 一、定义集合
# my_set = {"Python", "PHP", "Java", "C++", "C#", "Java", "PHP"}
# my_set_empty = set()  # 定义空集合
# print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")
# print(f"my_set_empty的内容是：{my_set_empty}，类型是：{type(my_set_empty)}")

my_set = {"Python", "PHP", "Java", "C++", "C#", "Java", "PHP"}
# 二、序列的操作————添加新元素
my_set.add("JavaScript")  # 在集合里面添加一个元素
my_set.add("PHP")  # 在集合里面添加一个元素
print(f"my_set添加新元素后的结果：{my_set}")
