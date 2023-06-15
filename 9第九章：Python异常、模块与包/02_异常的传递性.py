"""
    Python异常、模块与包：异常的传递性
"""


# 异常的传递性
def fun1():
    print("这里是fun1开始")
    1 / 0
    print("这里是fun1结束")


def fun2():
    print("这里是fun2开始")
    fun1()
    print("这里是fun2结束")


def main():
    try:
        fun2()
    except Exception as e:
        print("异常错误：", e, Exception)


main()
