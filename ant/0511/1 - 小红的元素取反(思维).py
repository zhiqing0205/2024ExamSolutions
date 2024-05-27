n, k = map(int, input().split())
nums = list(map(int, input().split()))

cnt_neg = cnt_zero = cnt_pos = 0
for num in nums:
    if num < 0:
        cnt_neg += 1
    elif num == 0:
        cnt_zero += 1
    else:
        cnt_pos += 1

res = cnt_pos - cnt_neg
if k <= cnt_neg:
    res += 2 * k
elif k <= cnt_neg + cnt_zero:
    res += 2 * cnt_neg
else:
    res += 2 * cnt_neg - 2 * (k - cnt_neg - cnt_zero)

print(res)