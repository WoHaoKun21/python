"""
    Python包：安装第三方Python包
        ① 安装过程：
            * 打开命令提示符程序（终端）
            * 在终端中输入pip install 包名称 / 也可以在PyCharm中进行第三方包的安装
            * 安装完毕后，可使用import进行导入
        ② pip install 安装包是通过国外的网进行连接
            解决：使用”pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称“，通过这个网址去下载包
"""
import numpy
import pandas

print(numpy, pandas)
