"""
Python的数据类型：使用type()进行监测数据类型
"""
# 方式一、使用print输出数据类型信息
print(type("这是一串字符串"))  # <class 'str'>
print(type(66))  # <class 'int'>
print(type(13.4))  # <class 'float'>

# 方式二、使用变量存储type()语句的结果
string_type = type("我是一名程序员")
int_type = type(66)
float_type = type(13.4)
print(string_type)
print(int_type)
print(float_type)

# 方式三、使用type()语句，查看变量中的数据类型信息
name = 'tom'
name_type = type(name)
print(name_type)
