S = input()
T = input()

flag = True
for i in range(len(S)):
    if len(S) > len(T):
        flag = False
        break
    if not S[i] == T[i]:
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')