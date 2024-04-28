def max_xor_sum(n, k, arr):
    # 初始化dp数组
    dp = [[float('-inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # 不分段的情况下异或和为0
    
    # 计算前缀异或
    prefix_xor = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_xor[i] = prefix_xor[i-1] ^ arr[i-1]
    
    # 填充dp数组
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            for l in range(j-1, i):
                dp[i][j] = max(dp[i][j], dp[l][j-1] + (prefix_xor[i] ^ prefix_xor[l]))
    
    # 返回结果
    return dp[n][k]

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(max_xor_sum(n, k, arr))