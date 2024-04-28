n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))
MOD = 10**9+7
dp = [[-1]*(sum(arr)+1) for _ in range(n+1)]
def dfs(i,p):
    if i == n:
        return 1 if p >= k else 0
    if dp[i][p] != -1:
        return dp[i][p]
    cnt = 0
    if p >= k:
        cnt += dfs(i+1,arr[i]) + dfs(i+1,p+arr[i])
    else:
        cnt += dfs(i+1,p+arr[i])
    cnt %= MOD
    dp[i][p] = cnt
    return dp[i][p]

print(dfs(0,0))
