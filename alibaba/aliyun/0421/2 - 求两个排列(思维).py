from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = []

mp = defaultdict(list)
for i in range(n):
    x = abs(i - (n - 1 - i))
    b.append(x)
    mp[x].append((i, n - 1 - i))

if all(x == y for x, y in zip(sorted(a), sorted(b))):
    p, q = [], []
    for i in range(n):
        x, y = mp[a[i]].pop()
        p.append(x + 1)
        q.append(y + 1)
    print(' '.join(map(str, p)))
    print(' '.join(map(str, q)))
else:
    print("-1")