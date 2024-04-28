n, m = map(int, input().split())
g = list(input().split())
def solve(s):
    s = list(map(int, s))
    one_cnt = sum(s)
    cnt_k = max_k = 0
    zeros = []
    for i in range(m):
        if s[i] == 1:
            cnt_k += 1
            max_k = max(max_k, cnt_k)
        else:
            cnt_k = 0
            zeros.append(-i)
    return [one_cnt, max_k, zeros]

a = []
for i, v in enumerate(g):
    a.append(solve(v) + [i + 1])

a.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
print(' '.join(str(x[3]) for x in a))