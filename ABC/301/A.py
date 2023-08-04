N = int(input())
S = input()

cntT = 0
cntA = 0
for i in range(N):
    if S[i] == 'T':
        cntT += 1
    elif S[i] == 'A':
        cntA += 1

if cntT != cntA:
    if cntT < cntA:
        print('A')
    else:
        print('T')
else:
    if S[-1] == 'T':
        print('A')
    else:
        print('T')
    
# S [-1]はSの最後