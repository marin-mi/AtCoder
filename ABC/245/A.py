A, B, C, D = map(int, input().split())

flag = True
if A < C:
    pass
elif A > C:
    flag = False
else:
    if B <= D:
        pass
    else:
        flag = False

if flag:
    print('Takahashi')
else:
    print('Aoki')
