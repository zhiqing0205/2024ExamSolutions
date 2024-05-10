n = int(input())
a = list(map(int, input().split()))
mx, s = max(a), sum(a)
res = [0] * n

def check(x, p):
    if x % 2 == 0:
        x -= 1
    
    p += x // 2 + 1
    return s + x <= p * n

for i in range(n):
    if a[i] == mx:
        res[i] = s
    elif n == 2:
        res[i] = -1
    else:
        l, r = 1, 10 ** 9
        while l < r:
            mid = (l + r) // 2
            if check(mid, a[i]):
                r = mid
            else:
                l = mid + 1
        res[i] = s + l

print('\n'.join(map(str, res)))