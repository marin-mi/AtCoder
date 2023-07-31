S = input()

flag = True

for i in range(len(S)):
    if len(S) < 4:
        flag = False
        break
    elif S[0] == 'Y' and S[1] == 'A' and S[2] == 'K' and S[3] == 'I':
        pass
    else:
        flag = False
    
if flag:
    print('Yes')
else:
    print('No')