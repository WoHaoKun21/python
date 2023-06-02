"""
    Python数据容器：字典的常用操作
        ① 新增元素：字典["key"]=value，原字典有当前key则进行修改value，没有则添加新的key和value
        ② 更新元素：字典["key"]=value，对字典中原有的key进行修改
        ③ 删除元素：字典.pop(key)，返回指定key的value，同时字典被修改，指定的key的数据被删除
        ④ 清空元素：字典.clear()，字典被修改，元素被清空
"""
# # 一、新增元素：字典["key"]=value
# my_dict = {"小樱": 73, "王小明": 80, "知世": 92}
# my_dict["艾利欧"] = 98  # 在字典中新增一个没有的key-value值
# print(f"新增元素后的结果为：{my_dict}")

# # 二、更新元素：字典["key"]=value
# my_dict = {"小樱": 73, "王小明": 80, "知世": 92}
# my_dict["知世"] = 85  # 修改字典内已有元素的value值
# print(f"修改小樱成绩后的结果为：{my_dict}")

# # 三、删除元素：del 字典["管家仔"] / 字典.pop(key)
# my_dict = {"小樱": 73, "王小明": 80, "知世": 92, "管家仔": 80, "路人": 33}
# del my_dict["管家仔"]  # 删除字典内的某个元素
# print(f"删除字典中“管家仔”后的结果为：{my_dict}")
# ele = my_dict.pop("路人")  # 删除字典内的某个元素
# print(f"删除字典中 “路人” 后的结果为：{my_dict}")

# # 四、清空元素：字典.clear()
# my_dict = {"小樱": 73, "王小明": 80, "知世": 92}
# my_dict.clear()  # 清除字典中所有的元素
# print(f"清除my_dict字典中所有元素后的结果为：{my_dict}")

# # 五、获取全部的key：字典.keys()
# my_dict = {"小樱": 73, "王小明": 80, "知世": 92}
# key_list = my_dict.keys()  # 拿到字典中所有的key
# print(f"获取my_dict中所有key组成的列表：{key_list}")

# # 六、遍历字典
# my_dict = {"小樱": 73, "王小明": 80, "知世": 92}
# #     6.1
# keys = my_dict.keys()  # 拿到字典中所有的key
# for i in keys:  # 遍历得到的keys
#     print(f"1遍历my_dict的元素 {i} 的成绩为：{my_dict[i]}")
# #     6.2
# for i in my_dict:  # 遍历得到的keys
#     print(f"2遍历my_dict的元素 {i} 的成绩为：{my_dict[i]}")

# # 七、统计字典内的元素数量：len(字典)
# my_dict = {"小樱": 73, "王小明": 80, "知世": 92}
# print(f"字典my_dict的长度为{len(my_dict)}")

# 练习：对员工信息使用字典进行数据记录——循环遍历，级别为1的员工，级别上升1级，薪水增加1000元
staff_info = {
    "小樱": {"部门": "科技部", "工资": 3000, "级别": 1},
    "王小明": {"部门": "市场部", "工资": 5000, "级别": 2},
    "知世": {"部门": "市场部", "工资": 7000, "级别": 3},
    "月": {"部门": "科技部", "工资": 4000, "级别": 1},
    "小可": {"部门": "市场部", "工资": 6000, "级别": 2}
}
print(f"全体员工当前信息如下：{staff_info}")

for name in staff_info:
    if staff_info[name]["级别"] == 1:
        staff_info[name]["级别"] += 1
        staff_info[name]["工资"] += 1000
print(f"员工升值加薪后的结果为：{staff_info}")
