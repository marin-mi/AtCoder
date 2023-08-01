N = int(input())
A = list(map(int, input().split()))

cnt = 0
B = []
for i in range(N):
    for j in range(7):
        cnt +=  A[7 * i + j]    
    B.append(cnt)
    cnt = 0
print(B)
print(*B)    