"""
    Python中while循环和for循环中的continue和break
        作用：循环重复的过程中，会出现一些其他情况让我们不得不停止这次循环，直接进入下次循环或者直接停止循环
            ① continue：中断所在循环的当次循环，直接进入下一次循环
            ② break：直接结束所在循环
"""

# # 一、循环的中使用continue
# for i in range(1, 6):
#     print("for循环中continue前的语句")
#     continue  # continue后的代码不会执行，直接进入下一次循环
#     print("for循环中continue后的语句")
# i = 0
# while i < 10:
#     print("while循环中continue前的语句")
#     i += 1
#     continue  # continue后的代码不会执行，直接进入下一次循环
#     print("while循环中continue后的语句")

# # 二、嵌套循环的中使用continue
# for i in range(1, 5):
#     print('外层循环1')
#     for j in range(1, 3):
#         print('内层循环2')
#         continue
#         print('内层循环3')
#     print("外层循环4")
#
# i = 0
# while i < 5:
#     print("while语句1")
#     j = 0
#     while j < 2:
#         print("while语句2")
#         j += 1
#         continue
#         print("while语句3")
#     print("while语句4")
#     i += 1

# # 三、循环的中使用break
# for i in range(1, 101):
#     print("for循环语句1")
#     break  # 结束整个for循环
#     print('for循环语句2')
# print('for循环结束语句3')
#
# i = 1
# while i < 101:
#     print('while循环语句1')
#     break  # 结束整个while循环
#     print('while循环语句2')
# print('while循环结束语句3')

# 三、嵌套循环的中使用break
for i in range(1, 5):
    print('for嵌套循环语句1')
    for j in range(1, 3):
        print('for循环嵌套语句2')
        break
        print('for循环嵌套语句3')
    print('for循环嵌套语句4')

i = 1
while i < 5:
    print('while嵌套循环语句1')
    j = 1
    while j < 5:
        print('while嵌套循环语句2')
        break
        print('while嵌套循环语句3')
    print('while嵌套循环语句4')
    i += 1
