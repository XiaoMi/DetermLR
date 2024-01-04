import json

# 用于存储visited nodes除以reasoning history元素个数的列表
average_visited_nodes_values = []

# 从JSON文件中读取数据
with open('proofwriter-visited-nodes.json', 'r') as json_file:
    data = json.load(json_file)

# 遍历JSON对象并计算visited nodes除以reasoning history元素个数的平均值
for entry in data:
    visited_nodes = entry.get("visited nodes", 0)  # 默认为0，以防找不到visited nodes字段
    reasoning_history = entry.get("reasoning history", [])
    reasoning_history_count = len(reasoning_history)

    if reasoning_history_count > 0:
        average_visited_nodes = visited_nodes / reasoning_history_count
        average_visited_nodes_values.append(average_visited_nodes)

# 计算整体的平均值
overall_average_visited_nodes = sum(average_visited_nodes_values) / len(average_visited_nodes_values)

# 打印整体平均值
print("生成一个条件平均需要visited nodes值：", overall_average_visited_nodes)

# import json
#
# # 用于存储visited nodes值的列表
# visited_nodes_values = []
#
# # 从JSON文件中读取数据
# with open('proof_writer_ours_fullmethod_n_4.json', 'r') as json_file:
#     data = json.load(json_file)
#
# # 遍历JSON对象并提取visited nodes值
# for entry in data:
#     visited_nodes = entry.get("visited nodes", 0)  # 默认为0，以防找不到visited nodes字段
#     visited_nodes_values.append(visited_nodes)
#
# # 计算visited nodes的平均值
# average_visited_nodes = sum(visited_nodes_values) / len(visited_nodes_values)
#
# # 打印平均值
# print("平均visited nodes值：", average_visited_nodes)


