nums = list(map(int, input().split()))
target = int(input())

nums.sort()
res = ['S']
l, r = 0, len(nums) - 1
while l < r:
    mid = l + r >> 1
    print(nums[mid])
    if nums[mid] == target:
        res.append('Y')
        break
    elif nums[mid] < target:
        l = mid + 1
        res.append('R')
    else:
        r = mid - 1
        res.append('L')

if nums[l] == target or nums[mid] == target:
    if res[-1] != 'Y':
        res.append('Y')
else:
    res.append('N')
print(''.join(res))