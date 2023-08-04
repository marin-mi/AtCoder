N = int(input())
S = input()
T = input()

flag = False
for i in range(N):
    if S[i] == T[i]:
        flag = True
    elif (S[i] == '1' and T[i] == 'l') or (T[i] == '1' and S[i] == 'l'):
        flag = True
    elif (S[i] == '0' and T[i] == 'o') or (T[i] == '0' and S[i] == 'o'):
        flag = True
    else:
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')