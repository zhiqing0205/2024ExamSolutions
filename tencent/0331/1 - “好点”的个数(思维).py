n, m = map(int, input().split()) # 读取节点数和边数
is_good_point = [True] * n # 初始化所有节点均为好点

for _ in range(m):
    u, v, color = input().split() # 读取边的信息
    u, v = int(u) - 1, int(v) - 1 # 调整索引从0开始

    if color != 'R':
        # 如果边不是红色，标记两个节点不是好点
        is_good_point[u] = is_good_point[v] = False

# 计算好点的数量
good_points_count = sum(is_good_point)

print(good_points_count)