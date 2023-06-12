"""
    Python文件操作：文件的读取
"""
# 一、打开文件
f = open("E:/python/8第八章：Python文件操作/测试.text", "r", encoding="UTF-8")
# print(f"通过open函数打开的文件类型：{type(f)}")

# 二、读物文件——read([num])
content = f.read(1)  # 读取文件中num字节的内容，不写num，则表示读取全部内容
print(f"文件中读取到的内容：{content}")

# 三、读物文件——readLines()

# 四、读物文件——readLine()

# 五、for循环读取文件行

# 六、文件的关闭

# 七、with open 语法操作文件
