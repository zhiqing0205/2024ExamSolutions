from collections import deque, defaultdict

def bfs(start, n, graph):
    distances = [-1] * (n + 1)
    distances[start] = 0
    queue = deque([start])
    farthest_node = start
    max_distance = 0
    
    while queue:
        node = queue.popleft()
        current_distance = distances[node]
        
        for neighbor in graph[node]:
            if distances[neighbor] == -1:  # 未访问
                queue.append(neighbor)
                distances[neighbor] = current_distance + 1
                if distances[neighbor] > max_distance:
                    max_distance = distances[neighbor]
                    farthest_node = neighbor
    
    return farthest_node, max_distance, distances

def solve(n, graph):
    # 第一次 BFS 找到任意的最远点 A
    node_A, _, _ = bfs(1, n, graph)
    
    # 第二次 BFS 从 A 开始找到最远点 B，并得到所有点到 A 的距离
    node_B, diameter, dist_from_A = bfs(node_A, n, graph)
    
    # 从 B 开始得到所有点到 B 的距离
    _, _, dist_from_B = bfs(node_B, n, graph)
    
    # 计算每个点添加叶子后的直径
    results = []
    for i in range(1, n + 1):
        # 计算 f(i)
        f_i = max(dist_from_A[i], dist_from_B[i]) + 1
        results.append(max(diameter, f_i))
    
    return results

# 输入处理
n = int(input())
# 创建图
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

results = solve(n, graph)
print(' '.join(map(str, results)))
