n, m = map(int, input().split())
a = [input() for _ in range(n)]

res = 0
for i in range(n - 1):
    for j in range(m - 1):
        s = set()
        for k in range(2):
            for l in range(2):
                s.add(a[i + k][j + l])
        if len(s) == 4:
            res += 1

print(res)