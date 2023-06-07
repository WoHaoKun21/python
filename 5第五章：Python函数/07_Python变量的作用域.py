"""
    Python：变量的作用域：变量的作用域指的是变量的作用范围（变量在那里可用，在哪里不可用），主要分为全局变量和局部变量
    1、局部变量：
        ① 局部变量：局部变量是定义在函数体内部的变量，即只在函数体内部生效
        ② 局部变量的作用：在函数体内不，临时保存数据，即当函数调用完成后，则销毁局部变量
    2、全局变量：
        全局变量：指的是，在函数体内、体外都内生效的变量（只要将变量定义在函数外面即可）
    3、global关键字的作用：
        格式：
            def test_a():
                global num
                num = 200
"""

# # 一、局部变量
# def testA():
#     num = 100  # 在函数体内部生成的局部变量
#     print("函数体内部的变量num：", num)
#
#
# testA()
# print("函数体外部访问函数内的num变量：", num)  # 访问错误：函数体内部的变量为局部变量，在函数外部无法进行访问，并且函数调用完毕后会进行变量销毁

# # 二、全局变量
# num = 100
# def test_a():
#     print(f'test_a：{num}')  # 访问全局变量的num，并且输出变量num存储的数据
# def test_b():
#     print(f'test_b：{num}')  # 访问全局变量的num，并且输出变量num存储的数据
# test_a()
# test_b()
# print(num)

# 三、在函数内修改全局变量
num = 100


def test_a():
    print(f'test_a：{num}')


def test_b():
    # 解决让函数内部可以修改全局变量的操作：使用global关键字
    global num  # 和外部的num变量变为同一个或者外部没有num的话，相当于创建了一个全局变量
    num = 500
    print(f'test_a：{num}')


test_a()
test_b()
print(num)
