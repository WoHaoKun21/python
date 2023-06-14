"""
    Python文件操作：文件的读取
"""
# 一、打开文件：open(位置, 读/写/追加, 编码格式)
f = open("E:/python/8第八章：Python文件操作/测试.txt", "r", encoding="UTF-8")
# print(f"通过open函数打开的文件类型：{type(f)}")

# # 二、读物文件——read([num])
# content = f.read(6)  # 读取文件中num字节的内容，不写num，则表示读取全部内容
# print(f"文件中读取到一字节的内容：{content}")
# content = f.read()  # 如果程序中出现多次read，第下次的read会在上一次read读取的结尾接着进行读取
# print(f"文件中读取到全部的内容：{content}")

# # 三、读物文件——readlines()：读取文件的全部行，并且封装到列表中
# lines = f.readlines()  # 读取文件全部内容，并根据行封装到列表中
# print(f"lines对象的类型为：{type(lines)}")
# print(f"lines对象的内容是：{lines}")

# # 四、读物文件——readLine()：一次读取一行的内容
# line = f.readline()  # 一次只读取文件中一行的内容
# line2 = f.readline()
# line3 = f.readline()
# print(f"读取到第一行的内容是：{line}")
# print(f"读取到第二行的内容是：{line2}")
# print(f"读取到第三行的内容是：{line3}")

# # 五、for循环读取文件行
# for line in f:
#     print(f"每一行数据是：{line}")

# # 六、文件的关闭：close()
# f.close()  # 关闭文件对象，例：程序运行后无法删除文件，显示运行中。通过这个方法，就可以终止运行
# print(f)

# # 七、with open 语法操作文件；运行完毕后文件会自动关闭
# with open("E:/python/8第八章：Python文件操作/测试.text", "r", encoding="UTF-8") as f:
#     for line in f:
#         print(f"每一行数据是：{line}")

# 课后练习：通过文件读取操作读取指定文件，并统计itheima出现的次数
f = open("E:/python/8第八章：Python文件操作/word.txt", "r", encoding="UTF-8")
# count = f.read().count('itheima')  # 这是方法一
# 方法二
count = 0
for line in f:
    # line = line.strip()  # 对字符串进行规整，默认消除开头和结尾的空格或者换行，也可以指定消除
    # words = line.split(" ")  # 根据空格进行分割
    words = line.strip().split(" ")  # 对字符串进行规整，并根据空格进行分割，最后得到一个列表
    for word in words:
        if word == "itheima":  # 如果单词匹配，进行数量加1
            count += 1

print(f"文件内容的itheima出现了{count}次", )
f.close()  # 关闭文件
