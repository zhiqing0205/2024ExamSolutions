n = int(input())
colors = [''] + [ch for ch in input()]
f = list(range(n+1))

def find(x):
    if f[x] != x:
        f[x] = find(f[x])
    return f[x]

for _ in range(n - 1):
    u, v = map(int, input().split())
    if colors[u] == colors[v] == 'R':
        f[find(u)] = find(v)

f_ids = set(find(i) for i in range(1, n+1))
mp = {f_id: i for i, f_id in enumerate(f_ids)}

from collections import defaultdict
factors = [defaultdict(int) for _ in range(len(f_ids))]

for i in range(1, n+1):
    x = i
    for j in range(2, int(x**0.5) + 1):
        while x % j == 0:
            factors[mp[find(i)]][j] += 1
            x //= j
    if x > 1:
        factors[mp[find(i)]][x] += 1

mod = 10**9 + 7
ans = 1
for i in range(len(f_ids)):
    for k, v in factors[i].items():
        ans = ans * (v + 1) % mod

print(ans)