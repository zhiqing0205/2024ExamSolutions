n,q = list(map(int,input().split()))
G = [[] for _ in range(n + 1)]
edges = []
for _ in range(n-1):
    u,v,w = list(map(int,input().split()))
    edges.append((u,v,w))
    G[u].append((v, w))
    G[v].append((u, w))

ops = []
for _ in range(q):
    ops.append(list(map(int,input().split())))

# 定义常量
N = n+1

# 初始化全局变量
pre = [0] * N
par = [0] * N
bit = [0] * 30
f = [[0] * 30 for _ in range(N)]
depth = [0] * N

def dfs(u, parent):
    depth[u] = depth[parent] + 1
    f[u][0] = parent
    i = 1
    while i < 30 and bit[i] <= depth[u]:
        f[u][i] = f[f[u][i - 1]][i - 1]
        i += 1
    for v, w in G[u]:
        if v != parent:
            dfs(v, u)


def lca(x, y):
    if depth[x] < depth[y]:
        x, y = y, x
    for i in range(29, -1, -1):
        if depth[x] - depth[y] >= bit[i]:
            x = f[x][i]
    if x == y:
        return x
    for i in range(29, -1, -1):
        if f[x][i] != f[y][i]:
            x = f[x][i]
            y = f[y][i]
    return f[x][0]


def dfs_xor(u, fa):
    par[u] = fa
    for v, w in G[u]:
        if v != fa:
            pre[v] = pre[u] ^ w
            dfs_xor(v, u)

dfs(1, -1)
dfs_xor(1, -1)

# 逆向遍历，将删除边变为增加边，使用并查集来维护连通性
parent = [i for i in range(n + 1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x,y = find(x),find(y)
    if x == y:
        return
    parent[x] = y

del_edges = set()
for op in ops:
    if op[0] == 1:
        del_edges.add(op[1])

for i,edge in enumerate(edges):
    if i+1 not in del_edges:
        union(edge[0],edge[1])

ops.reverse()
ans = []
for op in ops:
    if op[0] == 1:
        u,v,w = edges[op[1]-1]
        union(u,v)
    else:
        u,v = op[1],op[2]
        if find(u) != find(v):
            ans.append(-1)
        else:
            p = lca(u,v)
            c = par[p]
            ans.append(pre[u]^pre[p]^pre[v]^pre[c])

ans.reverse()
print('\n'.join(map(str,ans)))