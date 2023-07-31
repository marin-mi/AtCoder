S = list(map(int, input().split()))

flag = True
for i in range(len(S) - 1):
    if S[i] > S[i + 1]:
        flag = False
for i in range(len(S)):
    if S[i] < 100 or S[i] > 675:
        flag = False
    elif S[i] % 25 != 0:
        flag = False

if flag:
    print('Yes')
else:
    print('No')