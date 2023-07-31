N, K, Q = map(int, input().split())
A = [int(input() for _ in range(Q))]

A_score = [K] * N 

for i in range(N):
    A_score[i] += 1
    A_score[:i] -= 1
    A_score[i + 1] -= 1

for i in range(N):
    if A_score[]
    A_score[i]  
    print(A_score[i + 1])
