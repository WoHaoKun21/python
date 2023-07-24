import turtle as t  # 将导入包的名字更改为t
import time  # 导入时间包


def draw_gap():  # 绘制数码管间隔
    t.penup()
    t.fd(5)


# 绘制单段数码管
def draw_line(draw):
    draw_gap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    draw_gap()
    t.right(90)


# 根据数字绘制七段数码管
def draw_digit(d):
    draw_line(True) if d in [2, 3, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if d in [0, 2, 3, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if d in [0, 2, 6, 8] else draw_line(False)
    t.left(90)
    draw_line(True) if d in [0, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else draw_line(False)
    t.left(180)
    t.penup()
    t.fd(20)


# 绘画操作功能
def draw_date(date):
    t.pencolor("red")  # 设置画图的颜色
    for i in date:  # 对传递进来的时间进行遍历
        draw_digit(eval(i))  # 将时间传递个指定方法进行绘制操作


def main():
    t.setup(800, 350, 100, 200)  # 设置图库的 宽、高、窗口左侧与屏幕左侧的像素距离、窗口顶部与屏幕顶部的像素距离
    t.penup()  # 设置画笔启动
    t.fd(-300)  # 设置笔画之间的间隔
    t.pensize(5)  # 设置画笔画出的线条粗细，括号里是数字，一般是1或者2；
    draw_date(time.strftime('%Y%m%d', time.gmtime()))  # 将时间传给方法，开始自动生成时间图画
    t.done()  # 暂停程序，停止画笔绘制，但绘图窗体不关闭，直到用户关闭Python Turtle图形化窗口为止


main()
