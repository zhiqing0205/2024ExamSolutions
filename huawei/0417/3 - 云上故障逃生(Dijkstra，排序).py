n = int(input())
g = [[] for _ in range(n)]
for i in range(n):
    g[i] = [int(x) for x in input().split()]

v = list(map(int, input().split()))
u = int(input())
x = int(input())

dist = [float('inf')] * n
dist[u] = 0
vis = [False] * n
for _ in range(n):
    min_dist = float('inf')
    min_idx = -1
    for i in range(n):
        if not vis[i] and dist[i] < min_dist:
            min_dist = dist[i]
            min_idx = i
    vis[min_idx] = True
    for i in range(n):
        if not vis[i] and g[min_idx][i] != -1:
            dist[i] = min(dist[i], dist[min_idx] + g[min_idx][i])

dist[u] = float('inf')

nodes = sorted(list(zip(dist, list(range(n)), v)))

s = 0
res = []
for d, i, v in nodes:
    if d == float('inf'):
        res = [i for i in range(n) if i != u]
        break
    s += v
    res.append(i)
    if s >= x:
        break

print(' '.join(map(str, res)))
