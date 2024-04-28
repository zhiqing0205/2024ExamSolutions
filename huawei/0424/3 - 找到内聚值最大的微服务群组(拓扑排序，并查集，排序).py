n = int(input())
to = list(map(int, input().split()))

f = list(range(n))
d = [0] * n

def find(x):
    if x != f[x]:
        f[x] = find(f[x])
    return f[x]

for i, v in enumerate(to):
    f[find(i)] = find(v)
    d[v] += 1

from collections import deque

q = deque()
for i in range(n):
    if d[i] == 0:
        q.append(i)

while q:
    u = q.popleft()
    d[to[u]] -= 1
    if d[to[u]] == 0:
        q.append(to[u])

s = set()
for i in range(n):
    s.add(find(i))

mp = {}
for i, v in enumerate(s):
    mp[v] = i

a = [[0] * 3 + [float("inf")] for _ in range(len(s))]
for i in range(n):
    index = mp[find(i)]
    if d[i]:
        a[index][0] += 1
        a[index][2] = max(a[index][2], i)
        a[index][3] = min(a[index][3], i)
    else:
        a[index][1] += 1

a.sort(key=lambda x: (-(x[0] - x[1]), -x[2]))

start = a[0][3]
res = [start]
s = {start}
while True:
    start = to[start]
    if start in s:
        break
    res.append(start)
    s.add(start)

print(' '.join(str(x) for x in res))