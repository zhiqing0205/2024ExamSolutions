n = int(input())
a = list(map(int, input().split()))
a.sort()

cnt = s = 0
for x in a:
    if x > s:
        cnt += x - s
    s += x

print(cnt)