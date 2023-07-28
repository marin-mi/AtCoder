s = list(input())
t = list(input())

s.sort()
t.sort(reverse = True)
#S = ''.join(s)
#T = ''.join(t)
if s < t:
    print('Yes')
else:
    print('No')