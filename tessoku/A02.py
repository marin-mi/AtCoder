N, X = map(int, input().split())
A = list(map(int, input().split()))

flag = False
for a in A:
    if a == X:
        flag = True
    else:
        pass
if flag:
    print('Yes')
else:
    print('No')

