n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

c.sort()
s = [ai + bi for ai, bi in zip(a, b)]
for x in c:
    for i in range(n):
        if s[i] >= x:
            s[i] += 1
        else:
            s[i] -= 1

print(sum(s))