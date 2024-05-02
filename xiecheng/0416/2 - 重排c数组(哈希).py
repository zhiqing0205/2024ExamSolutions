from collections import Counter

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

cnt = Counter(c)
res = 0
for i in range(n):
    s = a[i] + b[i]
    if cnt[s] != 0:
        res += 1
        cnt[s] -= 1

print(res)