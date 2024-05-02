n, m = map(int, input().split())

f = list(range(n + 1))
def find(x):
    if f[x] != x:
        f[x] = find(f[x])
    return f[x]

for _ in range(m):
    a, b = map(int, input().split())
    f[find(a)] = find(b)

from collections import defaultdict
from itertools import accumulate
cnt = defaultdict(int)

for i in range(1, n + 1):
    cnt[find(i)] += 1

a = [0]
for _, v in cnt.items():
    a.append(v)
a.sort()

s = list(accumulate(a))
res = float("inf")

n = len(s)
for i in range(1, n):
    res = min(res, a[i] * i - s[i] + (s[-1] - s[i - 1]) - a[i] * (n - i))

print(res)