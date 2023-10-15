N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

score = [0] * N
for i in range(N):
    for j in range(M):
        if S[i][j] == 'o':
            score[i] += A[j]
    score[i] += i + 1

if score[i] == max(score):
    print(0)
else:
    