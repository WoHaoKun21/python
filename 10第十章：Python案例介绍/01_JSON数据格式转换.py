"""
    Python案例介绍-本章节用来进行python代码回忆：JSON数据格式转换
"""
import json

# # 一、创建一个列表对象转换为JSON数据
# data = [{"name": "汤姆", "age": 19}, {"name": "Marry", "age": 20}]
# #       通过json.dumps(数据)方法将python数据转换为JSON数据
# json_str = json.dumps(data, ensure_ascii=False)  # 第二个参数表示是否展示参数，中文转换为json个时候会是ASCLL类型
# print(f"列表转换为JSON数据为：{json_str}，类型为：{type(json_str)}")

# # 二、创建一个字典对象转换为JSON数据
# data = {"name": "周树人", "addr": "浙江省绍兴市越城区"}
# json_str = json.dumps(data, ensure_ascii=True)  # 将“ensure_ascii”设置为true，转换后的JSON数据格式中文会战时为Ascll数字
# print(f"字典转换为JSON数据为：{json_str}，类型为：{type(json_str)}")

# 三、将JSON字符串转换为列表：使用json.loads(JSON数据)
l = '[{"name": "汤姆", "age": 19}, {"name": "Marry", "age": 20}]'
list_data = json.loads(l)  # 将指定JSON数据转换为python数据类型
print(f"JSON数据转换为列表对象为：{list_data}，类型为：{type(list_data)}")

# 四、将JSON字符串转换为字典：使用json.loads(JSON数据)
d = '{"name": "周树人", "addr": "浙江省绍兴市越城区"}'
dict_data = json.loads(d)
print(f"JSON数据转换为字典对象为：{dict_data}，类型为：{type(dict_data)}")

t_d = "{'name':'TOM'}"
# print(json.loads(t_d))  # 使用双引号包裹起来的JSON数据转换会出现错误
