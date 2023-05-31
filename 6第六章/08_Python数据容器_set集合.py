"""
    Python数据容器，set集合
        特点：不支持元素重复（自带去重功能），并且内容是无序的。而数据容器都是有序切可以支持重复元素，具有局限性
        操作：
            ① add：集合.set(元素)，将指定元素添加到集合内，改变原有集合
            ② remove：集合.remove(元素)，将指定元素从集合中进行移除，改变原有集合
            ③ pop：集合.pop()，从集合中随机取出一个元素，返回一个元素
            ④ clear：集合.clear()，将集合中的元素全部清除，改变原有集合
            ⑤ difference：集合1.difference(集合2)，取出集合1和2的差集(集合1有，而集合2没有的)，不改变原有集合并返回一个新的集合
            ⑥ difference_update：集合1.difference_update(集合2)，对比集合1和2，在集合1内，删除和集合2相同的元素，集合1发生改变，集合2不改变
            ⑦ union：集合1.union(集合2)，将集合1和集合2组合成一个新的集合，得到一个新的集合，不改变集合1和2
"""
# # 一、定义集合
# my_set = {"Python", "PHP", "Java", "C++", "C#", "Java", "PHP"}
# my_set_empty = set()  # 定义空集合
# print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")
# print(f"my_set_empty的内容是：{my_set_empty}，类型是：{type(my_set_empty)}")

my_set = {"Python", "PHP", "Java", "C++", "C#", "Java", "PHP"}
# # 二、序列的操作————添加新元素：add（改变原集合）
# my_set.add("JavaScript")  # 在集合里面添加一个元素
# my_set.add("PHP")  # 在集合里面添加一个元素
# print(f"my_set添加新元素后的结果：{my_set}")

# # 2.2、序列的操作————移除元素：remove（改变原集合）
# my_set.remove("PHP")  # 移除集合里面的元素
# print(f"移除PHP后的set集合结果是：{my_set}")

my_set2 = {"Python", "PHP", "Java", "C++"}
# # 2.3、序列的操作————随机取出一个元素：pop（不改变原集合）
# element = my_set2.pop()  # 随机取出集合中的某个元素
# print(f"从集合中随机取出的元素为：{element}")

# # 2.4、序列的操作————清空结合：clear（改变原有集合）
# my_set2.clear()  # 清除集合中的所有元素
# print(f"清除集合元素后的结果为：{my_set2}")

# # 2.5序列的操作————取出两个集合的差集：difference（集合1有，而集合2没有的）
# my_set_one = {1, 2, 3}
# my_set_Two = {1, 5, 6}
# new_my_set = my_set_one.difference(my_set_Two)  # 在集合1中取出集合2中不同的元素，并返回一个新的集合
# print(f"my_set_one和my_set_two两个集合的差集为：{new_my_set}")  # 结果：{ 2, 3 }
# print(f"取差集后，原有的my_set_one内容：{my_set_one}")
# print(f"取差集后，原有的my_set_Two内容：{my_set_Two}")

# # 2.6序列的操作————消除两个集合的差集：difference_update（集合1改变，集合2不改变）
# set1 = {1, 2, 3}
# set2 = {1, 5, 6}
# set1.difference_update(set2)  # 消除两个集合的差集，在set1内删除和set2相同的元素
# print(f"消除集合差集，原有的set1内容为：{set1}")
# print(f"消除集合差集，原有的set2内容为：{set2}")

# # 2.7序列的操作————两个集合合并为1个：union（不改变原有集合）
# set1 = {1, 2, 3}
# set2 = {1, 5, 6}
# assign_set = set1.union(set2)  # 将集合1和集合2进行合并，不对原有集合进行任何改变
# print(f"两集合合并后的结果是：{assign_set}")
# print(f"两集合合并后，set1的内容为：{set1}")
# print(f"两集合合并后，set2的内容为：{set2}")

# # 统计集合元素数量：len(集合)
# num_set = {1, 2, 3, 5, 6, 4, 5, 6}
# print(f"集合num_set内的元素数量有{len(num_set)}个")

# # 集合的遍历——使用for循环。不支持while循环，因为set不支持下标索引
# num_set = {1, 2, 3, 5, 6, 4, 5, 6}
# for i in num_set:
#     print(f"集合的元素有：{i}")

# 练习：定义一个列表对象：["Python", "Java", "C++", "PHP", "Tom", "red", "blue", "green"]
my_list = ["Python", "Java", "PHP", "C++", "Java", "PHP", "red", "blue", "red", "green"]
#   定义一个空数组，通过for循环遍历列表，在for循环中将列表的元素添加至集合，最终得到元素去重后的集合对象，并进行打印
empty_set = set()  # 定义一个空set集合
for ele in my_list:
    print(f"my_list列表的内容：{ele}")
    empty_set.add(ele)  # 将列表元素添加到集合里面
print(f"将列表元素添加到集合后的结果为：{empty_set}")  # 输出添加元素后的集合
