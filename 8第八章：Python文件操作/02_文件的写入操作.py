"""
    Python文件操作：文件的写入操作
"""
import time

# # 一、打开不存在的文件：open(位置, 读/写/追加, 编码格式)
# f = open("E:/python/8第八章：Python文件操作/test.txt", "w", encoding="UTF-8")  # 以写入的方式打开文件
#
# # 二、文件写入：f.write("内容")
# f.write("文件内容写入，并进行查看")  # 执行后并未真正写入文件，只是存在了缓冲区
#
# # 三、内容刷新：f.flush()
# f.flush()  # 当调用flush后，内容才会真正写入文件
# time.sleep(3500)  # 模拟程序没有执行完毕，内容在没有flush的情况下是否写入到文件中
#
# # 四、关闭文件
# f.close()  # 对文件进行关闭：close方法内置了flush功能的


# 打开已经存在的文件
f = open("E:/python/8第八章：Python文件操作/test.txt", "w", encoding="UTF-8")
f.write("Python程序员")
f.flush()
f.close()
