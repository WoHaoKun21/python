"""
    Python文件操作：文件的写入操作
"""
# 一、打开文件：open(位置, 读/写/追加, 编码格式)
f = open("E:/python/8第八章：Python文件操作/test.txt", "w", encoding="UTF-8")  # 以写入的方式打开文件

# 二、文件写入：f.write("内容")
f.write("文件内容写入，以及查看")  # 执行后并未真正写入文件，只是存在了缓冲区

# 三、内容刷新：f.flush()
# f.flush()  # 当调用flush后，内容才会真正写入文件

# 四、关闭文件
f.close()  # 对文件进行关闭
