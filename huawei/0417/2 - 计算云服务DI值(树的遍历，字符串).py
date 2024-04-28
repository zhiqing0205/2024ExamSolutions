from collections import defaultdict
m, n = map(int, input().split())

roots = set()
g = defaultdict(set)
danger = defaultdict(int)
general = defaultdict(int)

for _ in range(n):
    x, f, t, cnt = input().split()
    if f == '*':
        roots.add(x)
    g[f].add(x)
    if t == '0':
        danger[x] += int(cnt)
    else:
        general[x] += int(cnt)

res = 0
for root in roots:
    q = [root]
    while len(q) > 0:
        x = q.pop()
        for y in g[x]:
            q.append(y)
            danger[root] += danger[y]
            general[root] += general[y]

    if 5 * danger[root] + 2 * general[root] >= m:
        res += 1

print(res)