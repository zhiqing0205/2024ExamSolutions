t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    ps = []
    for i in range(0, len(nums), 2):
        ps.append([nums[i], nums[i + 1]])
    
    def is_parallel(p1, p2, p3, p4):
        return (p1[1] - p2[1]) * (p3[0] - p4[0]) == (p3[1] - p4[1]) * (p1[0] - p2[0])

    def dis(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def check(p1, p2, p3, p4):
        return is_parallel(p1, p2, p3, p4) and not is_parallel(p1, p4, p2, p3) and dis(p1, p4) == dis(p2, p3)

    if check(ps[0], ps[1], ps[2], ps[3]) or check(ps[0], ps[2], ps[1], ps[3]) or check(ps[0], ps[3], ps[1], ps[2]):
        print("Yes")
    else:
        print("No")