"""
    Python的字符串的定义和操作
        字符串详解：字符串是只读的，不能进行修改操作
            1、尽管字符串看起来并不像列表和元组那样，一看就是存放了许多数据的容器，但是，字符串同样也是数据容器的一员
            2、字符串也是一个字符串的容器，一个字符串可以存放任意数量的字符，例："itPython"，类似于[ i, t, P, y, t, h, o, n ]
"""
# # 一、通过下标索引取值
# my_str = "itPython and Tom"
# s1 = my_str[2]  # 通过下标获取字符串的内容
# s2 = my_str[-14]  # 通过反向下标的字符串内容
# # my_str[2] = "H"  # 报错，因为字符串是只读的，不可以进行修改
# print(f"通过下标2和下标-14得到的字符串s1和s2内容：{s1}-{s2}")

# # 二、index方法
# my_str = "itPython and Tom"
# index = my_str.index("and")  # 通过index方法的到指定内容在字符串的下标
# print(f"在字符串‘{my_str}’中查找‘and’，其起始下标是：{index}")

# # 三、replace方法
# my_str = "itPython and Tom"
# new_str = my_str.replace("Tom", "PHP真的很强大")  # 将匹配到的所有字符串替换为指定的内容
# print(f"将{my_str}内的Tom替换为 “PHP真的很强大” 后的结果为：{new_str}")

# # 四、split方法
# my_str = "Hello Python Now I Whil Learn It"
# new_list = my_str.split(" ")  # 根据指定内容，将字符串分割成一个列表
# print(f"将字符串{my_str}通过split切分后的结果为：{new_list}，类型是：{type(new_list)}")

# # 五、strip方法：用来进行字符串规整
# my_str = " 12myPython21 "
# new_str = my_str.strip()  # 不传入参数，就是去除首尾空格
# print(f"将‘{my_str}’使用strip进行整理后的结果：{new_str}")
# my_str = "12myPython21"
# new_str2 = my_str.strip("12")  # 通过字符串12按照单个字符串将原有的字符串的1和2进行消除，相当于去除1和2
# print(f"将‘{my_str}’使用strip进行整理后的结果：{new_str}")

# # 六、count方法：统计字符串中某字符串出现的次数
# my_str = "it it it as it"
# count = my_str.count("it")
# print(f"字符串‘{my_str}’中o出现的次数：{count}")

# # 七、len方法：统计字符串的长度
# my_str = "China is a powerful country"
# length = len(my_str)
# print(f"字符串{my_str}的长度：{length}")

# 练习：字符串的遍历——for和while
my_str = "China is a powerful country"
# # while循环遍历字符串
# i = 0
# while i < len(my_str):
#     print(f"while循环遍历得到的字符串内容：{my_str[i]}")
#     i += 1

# # for循环遍历字符串
# for ele in my_str:
#     print(f"for循环得到的字符串内容：{ele}")

# 练习：
my_strs = "itPython itCast boxuegu"
# 查找”it“出现次数
count = my_strs.count("it")
# 将字符串中的空格替换为|

# 按照|将字符串进行分割
