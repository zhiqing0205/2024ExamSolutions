n, m = map(int, input().split())
grid = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    grid[i] = [0] + list(map(int, input().split()))

dp = [[float('-inf') for _ in range(m + 1)] for _ in range(n + 1)]
dp[0][1] = dp[1][0] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

print(dp[n][m])