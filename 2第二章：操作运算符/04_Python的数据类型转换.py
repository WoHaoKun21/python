"""
Python的数据类型转换：int(x)、float(x)、str(x)。这三种方法都有返回结果
        万物皆可转字符串，但是字符串转为数字，一定要保证字符串里面都是数字
"""

# 一、使用将数字类型转换为字符串类型
num_str = str(66)  # 使用str方法，将整型类型的66转换为字符串类型
print(type(num_str), num_str)  # 输出转换后的类型，结果为字符串类型

# 二、将字符串类型转换为数字类型
float_str = str(11.34)  # 使用str方法将 浮点类型 转换为 字符串类型
print(type(float_str), float_str)  # 输出转换后的类型，以及转换后的数据

# 三、将字符串转换为整数类型
num = int("12")  # 将字符串转换为整数，引号内的内容必须为数字才可以转换
print(type(num), num)

# 四、将字符串转换为浮点数类型
num2 = float('13.4')  # 将字符串转换为浮点数，引号内的内容必须为数字才可以转换
print(type(num2), num2)

# 五、整数转浮点数
int_float = float(12)  # 将整数转换为浮点数
print(type(int_float), int_float)

# 六、浮点数转整数
float_int = int(13.6)  # 将浮点数转换为整数
print(type(float_int), float_int)
