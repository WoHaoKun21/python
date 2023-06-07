"""
    Python数据容器：字典
"""
# # 定义字典
# my_dict = {"小樱": 73, "王小明": 80, "知世": 92}  # 定义一个字典，拥有键值对，这是和集合的最大区别

# # 定义空字典
# my_empty_dict = dict()  # 定义一个空字典
# my_empty_dict2 = {}  # 定义空字典
# print(f"my_dict的内容是：{my_dict}，类型：{type(my_dict)}")
# print(f"my_empty_dict的内容是：{my_empty_dict}，类型：{type(my_empty_dict)}")
# print(f"my_empty_dict2的内容是：{my_empty_dict2}，类型：{type(my_empty_dict2)}")

# # 定义重复key值的字典
# my_dict = {"小樱": 73, "王小明": 80, "知世": 92, "小樱": 88}  # 拥有重复key的字典，后面的key值会覆盖前面的
# print(f"重复key的字典内容是：{my_dict}")

# # 从字典中基于key获取value
# my_dict = {"小樱": 73, "王小明": 80, "知世": 92}
# print(f"小樱的成绩：{my_dict['小樱']}")  # 通过key获得成绩值
# print(f"王小明的成绩：{my_dict['王小明']}")
# print(f"知世的成绩：{my_dict['知世']}")

# # 定义嵌套字典
# stu_score_dict = {
#     "小樱": {"语文": 77, "数学": 80, "英语": 70},
#     "王小明": {"语文": 90, "数学": 81, "英语": 66},
#     "知世": {"语文": 80, "数学": 89, "英语": 90}
# }
# print(f"学生的考试信息：{stu_score_dict}")

# 从嵌套字典中获取数据
stu_score_dict = {
    "小樱": {"语文": 77, "数学": 80, "英语": 70},
    "王小明": {"语文": 90, "数学": 81, "英语": 66},
    "知世": {"语文": 80, "数学": 89, "英语": 90}
}
score = stu_score_dict["王小明"]["语文"]
print(f"王小明的语文成绩：{score}")
score = stu_score_dict["小樱"]["英语"]
print(f"小樱的英语成绩：{score}")
score = stu_score_dict["知世"]["数学"]
print(f"知世的数学成绩：{score}")
