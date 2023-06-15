"""
    Python异常、模块与包：异常的捕获
"""
# 一、基本捕获语法
# 读取一个不存在的文件，出现异常，并终止运行后面的代码，使用try except进行异常捕获并处理
try:
    f = open("E:/python/9第九章：Python异常、模块与包/异常文件/异常.txt", "r", encoding="UTF-8")
except:
    print("异常出现，文件不存在，系统将自动为您创建该文件")
    f = open("E:/python/9第九章：Python异常、模块与包/异常文件/异常.txt", "w", encoding="UTF-8")

# # 二、捕获指定的异常
# try:
#     print(name)  # 会出现变量名未定义错误：NameError
#     # 1 / 0  # 会出现”ZeroDivisionError“错误，如果指定异常捕获的话，不会被捕获
# except NameError as e:  # 这里指定捕获变量名异常
#     print("出现了变量未定义的异常", NameError)

# # 三、捕获多个异常
# try:
#     # print(name)
#     1 / 0
# except (NameError, ZeroDivisionError) as e:
#     print("捕获多个异常：", NameError, ZeroDivisionError, e)

# 四、捕获所有异常
try:
    # print(name)
    f = open("E:/python/9第九章：Python异常、模块与包/异常文件/异常2.txt", "r", encoding="UTF-8")
    # 1 / 0
    # print("Hello Word")
except Exception as e:  # 捕获全部异常
    print("出现异常了：", Exception, e)
    f = open("E:/python/9第九章：Python异常、模块与包/异常文件/异常2.txt", "w", encoding="UTF-8")
else:  # 代码没有异常的时候，执行，可不写
    print("没有异常后执行的代码")
finally:  # finally表示的时无论如何是否异常都要执行的代码，常用来资源关闭
    print("文件关闭")
    f.close()
