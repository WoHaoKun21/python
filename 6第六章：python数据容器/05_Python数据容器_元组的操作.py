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

# # 元组的循环：for循环
# for element in tuple_list:
#     print(f"for循环遍历到的元组元素：{element}")


# # 如果修改元组内的内容是否会进行报错
# my_tuple = (1, 2, "Python", "PHP")
# my_tuple[0] = 10  # 会进行报错，元组元素不支持再次重新修改

# # 特殊：元组不可以修改，但是可以修改元组内的list列表
# my_tuple = (1, 2, ["Python", "PHP"], 10)
# my_tuple[2][0] = "myItem"  # 修改元组里面的list列表内容
# print(f"修改元组里面list列表后的内容变化：{my_tuple}")

"""
    元组的基本操作案例:
        定义一个元组，内容是：("王小明", 11, ["football", "music"])，记录的是一个学生的信息
        通过元组的方法进行：
            1、查询其年龄所在的下标位置
            2、查询学生的姓名
            3、删除学生爱好中的football
            4、增加爱好：coding到爱好list内
"""
stu_tuple = ("王小明", 11, ["football", "music"])
index = stu_tuple.index(11)  # 得到学生年龄的下标
print(f"王小明的年龄在元组中的下标为：{index}")
name = stu_tuple[0]  # 查询学生的姓名
print(f"该同学的姓名为：{name}")
del stu_tuple[2][0]  # 删除学生的篮球爱好
print(f"王小明的篮球爱好被删除后的信息：{stu_tuple}")
stu_tuple[2].insert(0, "coding")  # 添加爱好到元组内的list列表内
print(f"王小明的爱好变为coding后的结果：{stu_tuple}")
