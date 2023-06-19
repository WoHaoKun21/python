"""
    Python包：自定义Python包
"""
import my_package.my_module1

# # 一、通过import导入自定义包
# import my_package.my_module1
# import my_package.my_module2
#
# my_package.my_module1.info_print()
# my_package.my_module2.info_print2()

# # 二、通过from导入包
# from my_package import my_module1
# from my_package import my_module2
#
# my_module1.info_print()
# my_module2.info_print2()

# # 三、通过from导入包的具体功能
# from my_package.my_module1 import info_print
# from my_package.my_module2 import info_print2
#
# info_print()
# info_print2()

# 四、通过__all__变量，控制import *：__all__写在__init__.py文件中
from my_package import *  # 导入被导出的指定模块，在__init__.py文件中进行查看

my_module1.info_print()
