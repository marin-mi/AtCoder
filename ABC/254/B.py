N = int(input())

A = [[0] * N for i in range(N)]

for i in range(N):
    for j in range(i + 1):
        if j == 0 or i == j:
            A[i][j] = 1
        else:
            A[i][j] = A[i - 1][j - 1] + A[i - 1][j]

for i in range(N):
    print(*A[i][:i + 1])

# sano192の記事を参考にした
# 二次元配列に入れてから出力する
