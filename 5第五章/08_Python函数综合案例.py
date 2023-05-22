"""
    Python：函数的综合案例：ATM机的实现
"""

name = input("请输入您的用户名：")  # 存储姓名
money = 50000  # 存储余额


def menu():  # 主菜单函数
    print("--------------主菜单---------------")
    print(f"{name}，您好，欢迎使用自助ATM机，请选择操作：")
    print(f"查询余额\t[输入1]")
    print(f"存款\t\t[输入2]")
    print(f"取款\t\t[输入3]")
    print(f"退出\t\t[输入4]")
    return int(input("请输入您的选择："))


def money_search(show):  # 余额查询函数
    if show:
        print("--------------查询余额---------------")
    print(f"{name}，您好，你当前的余额为：{money}元")


def money_save_pull(title, num):  # 存或取款函数
    global money
    print(f"--------------{title}---------------")
    if title == "存款":
        money += num
        print(f"{name}，您好，您存款{num}元成功")
        money_search(False)
    elif title == "取款":
        last_money = money
        money -= num
        if money < 0:
            money = last_money
            money_save_pull("取款", int(input("对不起，您的余额不足，请重新输入金额：")))
        print(f"{name}，您好，您取款{num}元成功")
        money_search(False)


while True:
    key = menu()
    if key == 1:
        money_search(True)
        continue
    elif key == 2:
        money_save_pull("存款", int(input("请输入存款金额：")))
        continue
    elif key == 3:
        money_save_pull("取款", int(input("请输入取款金额：")))
        continue
    else:
        print("退出成功")
        break
