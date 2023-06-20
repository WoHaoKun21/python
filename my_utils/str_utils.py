def str_reverse(strs):  # 对字符串进行反转
    """
    将字符串进行反转
    :param strs: 将要被反转的字符串
    :return: 返回反转后的字符串
    """
    return strs[::-1]  # 返回的是饭庄后的字符串


def substr(strs, start, end):  # 进行字符串切片
    """
    按照给定下标返回字符串的切片
    :param strs: 给定的字符串
    :param start: 字符串切片起始下标
    :param end: 字符串结束下标
    :return: 返回切片后的下标
    """
    return strs[start:end]  # 返回的是进行切片后的字符串


if __name__ == "__main__":
    str_reverse("abcdefg")
    substr("abcdefg", 0, 2)
