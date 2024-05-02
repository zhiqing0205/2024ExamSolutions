class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]

def count_ways(n, edges):
    uf = UnionFind(n)
    
    # 合并图中已经连接的节点
    for u, v in edges:
        uf.union(u - 1, v - 1)  # 减1是因为输入的节点编号从1开始，而数组索引从0开始

    # 统计每个连通分量的大小
    component_size = [0] * n
    for i in range(n):
        root = uf.find(i)
        component_size[root] += 1

    # 计算不同的加边方案
    ways = 0
    for size in component_size:
        if size > 0:
            ways += size * (n - size)
    
    # 由于每种方案被计算了两次，需要除以2进行修正
    ways //= 2
    return ways

# 输入处理
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# 计算结果
print(count_ways(n, edges))