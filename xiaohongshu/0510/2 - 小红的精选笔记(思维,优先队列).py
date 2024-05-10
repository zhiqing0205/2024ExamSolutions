import heapq

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = sorted(zip(a, b), key=lambda x: -x[1])

s = 0
q = []
res = 0
for i, (ai, bi) in enumerate(c):
    if i < k:
        s += ai
        # 用小根堆维护最大的k个数，这样最小的数就在堆顶
        heapq.heappush(q, ai)
    else:
        # 如果当前数比堆顶小，就替换堆顶
        if q[0] < ai:
            s += ai - q[0]
            heapq.heappop(q)
            heapq.heappush(q, ai)
        res = max(res, s * bi)

print(res)