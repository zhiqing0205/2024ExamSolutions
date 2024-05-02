n = int(input())
a = list(map(int, input().split()))

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

b = []
i = 0
res = 0
for i in range(n):
    b.append(a[i])
    if len(b) > 1:
        x = b.pop()
        y = b.pop()
        if x == 2 and is_prime(y) and is_prime(y + 2):
            b.append(y + 2)
            res += 1
        elif y == 2 and is_prime(x) and is_prime(x + 2):
            b.append(x + 2)
            res += 1
        else:
            b.append(y)
            b.append(x)

i = 0
while i + 1 < len(b):
    if is_prime(b[i]) and is_prime(b[i + 1]):
        res += 1
        i += 1
    i += 1

print(n - res)