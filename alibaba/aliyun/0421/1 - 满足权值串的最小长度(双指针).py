n, k = map(int, input().split())
s = input()

res = float("inf")
l = 0
current = 0
for r in range(1, n):
    if s[r] == s[r - 1]:
        current += 1
    
    while current > k and l < r:
        if s[l] == s[l + 1]:
            current -= 1
        l += 1
    
    if current == k:
        res = min(res, r - l + 1)

print(res if res < float("inf") else -1)