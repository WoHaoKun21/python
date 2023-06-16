__all__ = ["add"]  # 之作用在*上


def add(a, b):
    print(a + b)
    return a + b


def sub(a, b):
    print(a - b)
    return a - b

# if __name__ == '__main__':  # 当我们在这个页面调用的时候内置变量__name__就会变为__main__
#     add(2, 3)
