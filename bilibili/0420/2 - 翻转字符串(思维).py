n, k = map(int, input().split())
s = input()

if (n - k) % 2 != 0:
    print(s[k - 1:] + s[:k - 1])
else:
    print(s[k - 1:] + s[:k - 1][::-1])