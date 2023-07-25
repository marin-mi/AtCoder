S = input()
T = input()

flag = False
for i in range(len(S)):
    for j in range(len(S) + 1):
        if S[i:j] == T:
            flag = True
if flag:
    print('Yes')
else:
    print('No')
    
