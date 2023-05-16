"""
    Python中for循环的基础+range语句的使用
        格式：range(num)
"""
# # range()语法一：range(num)
# for i in range(10):
#     print("range语法一：", i)

# # range()语法二：range(num1, num2)
# for i in range(2, 10):
#     print("range语法二：", i)

# # range()语法三：range(num1, num2, 4)
# for i in range(2, 10, 4):  # 输出从2-10，不包含10，数字之间的间隔为4，默认为1
#     print("range语法三：", i)

# # range()语法配合for循环训练一：
# for i in range(10):
#     print(f"送出第{i + 1}朵玫瑰")

# range()语法配合for循环训练三：算出偶数个数
num = int(input("请输入数值："))
count = 0
for i in range(1, num):
    if i % 2 == 0:  # i%2表示能被2除尽的数值也就是偶数
        count += 1
print(f"数值之间共有{count}个偶数")
