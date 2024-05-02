s = input()
n = len(s)
res = 0
for i in range(n - 1):
    if s[i] == 'y' and s[i + 1] == 'u':
        res += 1

print(res)