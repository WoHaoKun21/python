"""
Python的字符串扩展：
    1、字符串的三种定义方式：单引号定义法、双引号定义法、三引号定义法
    2、字符串拼接：将两个不同的字符串变量进行拼接
    3、字符串格式化：解决变量过多和字符串无法与其他类型进行拼接的问题
    4、格式化的精度控制
    5、字符串格式化方式2
    6、对表达式进行格式化
"""

# # 1、字符串的三种定义方式：单引号定义法、双引号定义法、三引号定义法
# name = '单引号定义字符串'
# print(name, type(name))
# name = "双引号定义字符串"
# print(name, type(name))
# name = """三双引号字符串"""
# print(name, type(name))
# name = '''三单引号字符串'''
# print(name, type(name))

# # 2、字符串的拼接：常用于字面量和变量之间进行拼接
# print("学无止尽" + "贵在坚持")
# name = "Python"
# address = "杭州富阳"
# tel = 15022367746
# # print('我在' + address + '学习' + name + '我的电话是：' + tel)  # 类型错误，字符串类型不能和其它类型进行拼接

# # 3、字符串格式化：解决变量过多或拼接其他类型错误的问题
# work = 'Python'
# address = '杭州富阳'
# tel = 15022364458
# message = "我在%s学习Python技术" % address  # %s：% 表示我要占位，s 表示将变量放入占位的地方
# print(message)
# message = "我在%s学习%s技术,我的电话是：%d" % (address, work, tel)  # 存在多个占位变量的时候要使用()包裹起来，并且按顺序写入变量名称
# print(message)
# china = '新中国'
# year = 1949
# age = 23.5
# message = "%s成立于%d，距离现在已经过去73年了，今年我已经%f岁了" % (china, year, age)  # %s：将变量转换为字符串；%d将变量转换为整数；%f：转换为浮点型
# print(message)

# # 4、格式化的精度控制：解决字符串占位符%f后面的小数精确度
# num1 = 11
# num2 = 11.456
# print("数字11宽度限制为5，结果是%5d" % num1)
# print("数字11宽度限制为1，结果是%1d" % num1)
# print("数字11.456宽度限制5，小数精度2，结果是%7.2f" % num2)  # 会进行四舍五入
# print("数字11.456不限制，小数精度2，结果是%.2f" % num2)  # 会进行四舍五入

# # 5、字符串格式化第二种方式：不理会类型、不做精度处理
# name = '新中国'
# year = 1949
# people = 14.5
# message = f"{name}成立于{year}年，距今已有73年，总人口约{people}亿人口"
# print(message)

# # 6、对表达式进行格式化
# print("11 * 11的结果是：%d" % (11 * 11))
# print(f"1 * 1的结果是：{1 * 1}")
# print("字符串在Python中的类型是：%s" % type("字符串"))
# print(f"字符串在Python中的类型是：{type('字符串')}")

# 练习：股价计算
name = "股价公司"  # 公司名称
stock_price = 19.99  # 当前股价
stock_code = '003032'  # 股价代码
stock_price_daily_growth_factor = 1.2  # 股票每日增长系数
growth_days = 7  # 增长天数
finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days

print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增成长系数是：%.1f，经过%d天的增长后，股票达到了：%.2f" % (
    stock_price_daily_growth_factor, growth_days, finally_stock_price))
