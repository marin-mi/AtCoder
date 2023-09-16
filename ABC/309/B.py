N = int(input())
A = [input() for _ in range(N)]

B = [['0'] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0 and j > 0:
            B[i][j] = A[i][j - 1]
        elif i > 0 and j == N - 1:
            B[i][j] = A[i - 1][j]
        elif i == N - 1 and j < N - 1:
            B[i][j] = A[i][j + 1]
        elif i < N - 1 and j == 0:
            B[i][j] = A[i + 1][j]
        else:
            B[i][j] = A[i][j]

for i in range(N):
    print(*B[i], sep='')

# kiwamaさんの回答を参考にした
# 外壁は全部で4パターン
# 19行目はprint(''.join(B[i]))でも可能
