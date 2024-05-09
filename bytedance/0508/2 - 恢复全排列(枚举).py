n = int(input())
a = list(map(int, input().split()))

for i in range(1, n + 1):
    p = [i]
    s = {i}
    for j in range(1, n):
        x = a[j - 1] - p[j - 1]
        p.append(x)
        if x <= 0 or x > n or x in s:
            break
        s.add(x)
    if len(s) == n:
        print(*p)
        break
else:
    print(-1)
