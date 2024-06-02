import heapq

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(0)
elif a[0] == a[-1]:
    print(1)
else:
    mx = max(a)
    edges = [[] for _ in range(mx + 1)]
    s = set(a)
    for x in s:
        for t in (x + x, mx + 1, x):
            if t in s:
                cost = t // x
                edges[x].append((t, cost))
                edges[t].append((x, cost))

    dist = [float('inf')] * (mx + 1)
    dist[a[0]] = 0
    q = [(0, a[0])]
    vis = [False] * (mx + 1)

    while q:
        d, u = heapq.heappop(q)
        if vis[u]:
            continue
        vis[u] = True
        for v, w in edges[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(q, (dist[v], v))

    print(dist[a[-1]] if dist[a[-1]] != float('inf') else -1)
