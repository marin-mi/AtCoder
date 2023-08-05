N = int(input())
P = list(map(int, input().split()))
 
max_ = P[0]
eqcnt = 0
cnt = 0    
   
for i in range(1, N - 1):
    if max_ < P[i]:
        max_ = P[i]
        cnt += 1
    elif P[0] == P[i]:
        eqcnt += 1
if eqcnt > 0 and cnt == 0:
    print(1)
else:
    if max_ == P[0] and cnt == 0:
        print(0)
    else:
        print(max_ + 1 - P[0])