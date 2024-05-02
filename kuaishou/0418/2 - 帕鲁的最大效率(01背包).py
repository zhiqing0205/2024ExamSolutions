V, n = map(int, input().split())
v = list(map(int, input().split()))
w = list(map(int, input().split()))

dp = [0] * (V + 1)
for i in range(n):
    for j in range(V, v[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - v[i]] + w[i])

print(dp[V])