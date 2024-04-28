from collections import deque

n, k = map(int, input().split())
nums = list(map(int, input().split()))
q = deque()

res = []
for i, num in enumerate(nums):

    # 入队时，将队列中比当前元素小的元素全部出队
    while q and nums[q[-1]] <= num:
        q.pop()
    q.append(i)
    
    # 出队时，判断队首元素是否在窗口内
    if i >= k - 1:
        res.append(nums[q[0]])
        if q[0] == i - k + 1:
            q.popleft()

print(' '.join(map(str, res)))