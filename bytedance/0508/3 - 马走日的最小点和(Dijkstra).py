import heapq

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
d = [[float('inf')] * m for _ in range(n)]

d[0][0] = map[0][0]
q = [(d[0][0], 0, 0)]
visited = [[False] * m for _ in range(n)]

while q:
    c, x, y = heapq.heappop(q)
    if visited[x][y]:
        continue
    visited[x][y] = True
    for dx, dy in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and d[nx][ny] > c + map[nx][ny]:
            d[nx][ny] = c + map[nx][ny]
            heapq.heappush(q, (d[nx][ny], nx, ny))

print(d[n - 1][m - 1] if d[n - 1][m - 1] != float('inf') else -1)