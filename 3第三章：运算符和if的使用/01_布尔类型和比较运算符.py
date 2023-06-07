"""
    Python的布尔类型和比较运算符
        常用比较运算符：==、!=、>、<、>=、<=
"""

# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}，类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2}，类型是：{type(bool_2)}")

# 比较运算符——等于（==）
num1 = 10
num2 = 10
print(f"10 == 10的结果是：{num1 == num2}")

# 比较运算符——不等于（!=）
num1 = 10
num2 = 15
print(f"10 != 15的结果是：{num1 != num2}")

name1 = 'item'
name2 = 'iteName'
print(f"item == iteName的结果是：{name1 == name2}")

# 比较运算符——大于（>）、小于（<）
num1 = 10
num2 = 5
print(f"10 > 5的结果是：{num1 > num2}")
print(f"10 < 5的结果是：{num1 < num2}")

# 比较运算符——大于等于（>=）、小于等于（<=）
num1 = 10
num2 = 10
print(f"10 >= 10的结果是：{num1 >= num2}")
print(f"10 <= 10的结果是：{num1 <= num2}")
