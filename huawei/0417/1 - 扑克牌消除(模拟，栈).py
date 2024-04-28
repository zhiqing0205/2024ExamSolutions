n = int(input())
lst = input().split()

s = []
for ch in lst:
    s.append(ch)
    if len(s) >= 3 and s[-1] == s[-2] == s[-3]:
        s.pop()
        s.pop()
        s.pop()

if len(s) == 0:
    print(0)
else:
    print(' '.join(s))