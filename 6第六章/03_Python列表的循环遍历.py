"""
    Python的数据容器：list（列表）的循环遍历
        1、while循环遍历列表
        2、for循环遍历列表
"""

# # while循环遍历列表
# def list_while_func():
#     my_list = ["Python", "C++", "Java", "PHP", "MySQL"]
#     index = 0
#     while index < len(my_list):
#         elem = my_list[index]
#         print(f"while循环遍历到的元素：{elem}")
#         index += 1
# list_while_func()


# # for循环遍历列表
# def list_for_func():
#     my_list = ["Python", 12, "C++", 5, "Java", "PHP"]
#     for element in my_list:
#         print(f"for循环遍历到的元素：{element}")
# list_for_func()

# 列表遍历练习：取出列表内的偶数
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# # 使用while循环进行解决
# def while_func():
#     arr = []
#     i = 0
#     while i < len(num_list):
#         if num_list[i] % 2 == 0:  # 取出偶数
#             arr.append(num_list[i])
#         i += 1
#     return arr
# new_arr = while_func()
# print(f"列表的偶数：{new_arr}")

# 使用for循环进行解决
def for_func():
    arr = []
    for ele in num_list:
        if ele % 2 == 0:
            arr.append(ele)
    return arr


new_arr2 = for_func()
print(f"通过for循环得到的偶数列表：{new_arr2}")
