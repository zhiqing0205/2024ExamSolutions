def find_paths(matrix):
    n, m = len(matrix), len(matrix[0])
    target = "tencent"
    dp = [[[0 for _ in range(len(target) + 1)] for _ in range(m)] for _ in range(n)]
    
    # 初始化
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target[0]:
                dp[i][j][1] = 1

    # 动态规划填表
    for step in range(2, len(target) + 1):
        for x in range(n):
            for y in range(m):
                if matrix[x][y] == target[step - 1]:
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            dp[x][y][step] += dp[nx][ny][step - 1]

    # 计算总路径数
    total_count = sum(dp[x][y][-1] for x in range(n) for y in range(m))
    
    return total_count

n, m = map(int, input().strip().split())
matrix = [input().strip() for _ in range(n)]

print(find_paths(matrix))