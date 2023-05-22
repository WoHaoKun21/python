"""
    Python的数据容器：list（列表）
"""

# # 一、list（列表）的使用
# name_list = ['Python', 'C++', 'Java', 'PHP']
# print(name_list)
# print("name_list的数据类型：", type(name_list))

# # 二、list（列表）的混合类型元素
# my_list = ['Python', 125, True]  # 列表中存储不同的类型元素
# print(my_list)
# print("my_list的数据类型：", type(my_list))

# # 三、嵌套list（列表）
# my_list_any = ["Python", [1, 2, 3], 3, [4, 5, 6], False]
# print("嵌套列表：", my_list_any)
# print("嵌套列表类型：", type(my_list_any))

# # 四、通过下标索引获取列表元素
# my_list2 = ['Python', 'C++', 125, 'Java', False, 'PHP']
# print(my_list2[2])  # 通过索引获取指定列表里面的元素
# print(my_list2[4])  # 通过索引获取指定列表里面的元素
# print(my_list2[-5])  # 从右往左数第五个

# # 五、通过下标索引获取列表元素（倒序取出）
# my_list3 = ['Python', 'C++', 'PHP']
# print(my_list3[-1])
# print(my_list3[-2])
# print(my_list3[-3])

# 六、取出嵌套列表的元素
my_list_any2 = ["Python", [1, 2, 3], 3, [4, 5, 6], False]
print(my_list_any2[1][0])  # 取出嵌套列表里面的列表元素中的元素
