"""
    Python案例介绍：pyecharts模块快速入门
"""
# 一、构建一个基础折线图
# 导包：导入Line功能构建折线对象
from pyecharts.charts import Line

line = Line()  # 得到折线对象
line.add_xaxis(["中国", "英国", "美国"])  # 添加x轴数据
line.add_yaxis("GDP", [30, 20, 10])  # 添加y轴数据
line.render()  # 将代码生成图表——会生成一个echarts的html文件
