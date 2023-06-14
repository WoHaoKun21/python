"""
    Python文件操作综合案例：对bill.txt文件进行操作
        需求：
            1、读取文件
            2、将文件写出到bill.txt.bak文件作为备份
            3、同时将文件内标记为测试的数据行丢弃
"""
# 一、读取文件
fr = open("E:/python/8第八章：Python文件操作/bill.txt", "r", encoding="UTF-8")

# 二、将文件内容中标识为测试的数据进行清除，然后备份到bill.txt.bak文件中
fw = open("E:/python/8第八章：Python文件操作/bill.txt.bak", "w", encoding="UTF-8")
# 我的思路：使用追加模式，通过for循环进行逐条判断追加；但是还是要使用写入操作来进行，因为重复调用会追加重复
for line in fr:
    count = line.count('测试')  # 判断是否出现测试
    if count == 0:  # 如果行未出现测试，则对新的文件进行内容追加
        fw.write(line)

fr.close()  # 文件关闭，内部自带flush功能
fw.close()  # 文件关闭
