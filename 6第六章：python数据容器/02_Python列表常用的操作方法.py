"""
    Python的数据容器：list（列表）常用的操作方法
        ① 查询元素：[].index(参数)，传入内容，用来获取改内容在列表元素下标
        ② 插入元素
        ③ 删除元素
        ④ 清空元素
        ⑤ 修改元素
        ⑥ 统计元素个数
"""
myList = ["Python", "C++", "Java", "PHP", "MySql"]

# # 一、查询元素——[].index(下标)
# data = myList.index('Python')  # 查找该内容，在列表中的下标索引值
# print("得到的数据的下标索引：", data)
# # #        1.2 当查找的元素不存在，会进行报错
# # data = myList.index('JavaScript')  # 查找列表内不存在的元素，进行报错
# # print("得到的数据的下标索引：", data)

# # 二、修改特定下标索引的值：["Python", "C++", "Java", "PHP", "MySql"][1] = "元素"
# myList[1] = "C#"
# print("修改列表后的结果：", myList)

# # 三、在指定下标位置插入新元素：[].insert(下标, 元素)
# myList.insert(0, "JavaScript")  # 将内容插入到下标为0的位置
# print("通过列表insrt插入数据后的结果：", myList)

num_list = [1, 3, 5, 7, 9]

# # 四、在列表尾部追加一个新元素：[].append(元素)
# num_list.append(10)  # 在列表尾部追加一个元素
# print("使用列表尾部追加方法后的结果：", num_list)

# # 五、在列表尾部追加一批新元素：[].extend(批量数据)
# num_list.extend(["元素1", "元素2", "元素3"])  # 通过extend追加其它列表里面的数据
# print("列表追加新列表后的结果：", num_list)

# # 六、删除指定下标索引的元素——2种方法
# #   6.1 方式1：del 列表[下标]
# del num_list[4]  # 删除下标为4的元素
# print("del关键字删除列表元素后的结果：", num_list)
# #   6.2 方式2：列表.pop(下标)
# element = num_list.pop(2)  # 通过列表的pop方法删除指定下标的元素，并返回删除的元素
# print("pop方法删除元素后的结果：", num_list, "取出的元素是：", element)

num_repeat = [1, 5, 3, 5, 1, 5, "tom", 9, "tom"]
# # 七、删除某元素在列表中的第一个匹配项：[].remove(元素)
# num_repeat.remove("tom")  # 使用[]remove(元素)，会移除掉第一个匹配的元素
# print("使用remove移出数据后列表的结果：", num_repeat)

# # 八、清空列表：[].clear()
# num_repeat.clear()  # [].clear()会将列表内的所有元素进行清除
# print("使用clear清空列表后的结果：", num_repeat)

# # 九、统某元素在列表内出现的数量
# count = num_repeat.count(5)  # [].count(元素)，会统计在列表中的数量
# print(f"数字5在列表中的数量：{count}")

# # 十、统计列表中全部的元素数量：len(数据)，不属于列表的方法
# length = len(num_repeat)  # len(列表/元素)，用来统计元素的数量
# leng = len("字符串数据")
# print(f"列表的长度：{length}，字符串的长度：{leng}")

"""
    练习案例：一个列表-[21, 25, 21, 23, 22, 20]
        通过列表功能，对其进行操作
            1、定义这个列表，并用变量进行接受
            2、追加一个数字31到列表尾部
            3、追加一个新列表[29, 33, 30]，到列表的尾部
            4、取出第一个元素
            5、取出最后一个元素
            6、查找元素31在列表中的下标位置
"""
practice_list = [21, 25, 21, 23, 22, 20]  # 定义列表，并用变量进行接收
practice_list.append(31)  # 将31追加到列表尾部
practice_list.extend([29, 33, 30])  # 将[29, 33, 30]追加到列表尾部
first_elem = practice_list[0]  # 取出第一个列表元素
last_elem = practice_list[len(practice_list) - 1]  # 取出列表最后一个元素
last_elem = practice_list[-1]  # 使用反向索引取出列表最后一个元素
elem_index = practice_list.index(31)  # 得到31在列表内的下标
print(practice_list, first_elem, last_elem, elem_index)
