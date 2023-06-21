def print_file_info(path):  # 接受文件路径，并打印文件内的内容，不存在，在进行异常捕获进行提示
    """
    功能：查找文件的内容
    :param path: 文件的指定路径
    :return: None
    """
    f = None
    try:
        f = open(path, "r", encoding="UTF-8")
        print(f"该文件内容为：{f.read()}")  # 打印读取到的文件内容
    except Exception as e:  # 接受任何类型的错误
        print(f"很抱歉，您所查找的文件并不存在，具体原因为：{e}")
    finally:
        if f:  # 如果有文件数据，则进行关闭
            f.close()
        print("文件已经自动关闭")


def append_to_file(path, data):
    """
    功能：将指定的数据加入到指定的文件中
    :param path: 文件路径
    :param data: 在文件中要追加的数据
    :return: None
    """
    f = None
    try:
        f = open(path, "a", encoding="UTF-8")
        f.write(data)
    except Exception as e:  # 接受任何类型的错误
        print("很抱歉，您所查找的文件并不存在", e)
    finally:
        print("内容已添加到文件中")
        f.close()


if __name__ == "__main__":
    print_file_info("E:/python/9第九章：Python异常、模块与包/异常文件/异常.txt")
    append_to_file("E:/python/9第九章：Python异常、模块与包/异常文件/异常2.txt", "\n数据内容")
