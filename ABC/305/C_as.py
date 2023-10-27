H, W = map(int, input().split())
S = [input() for _ in range(H)]

U, D = 10 ** 9, - 10 ** 9
L, R = 10 ** 9, - 10 ** 9

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            U = min(U, i)
            D = max(D, i)
            L = min(L, j)
            R = max(R, j)

for i in range(U, D + 1):
    for j in range(L, R + 1):
        if S[i][j] == '.':
            print(i + 1, j + 1)

# 最小値、最大値の変数を大文字一文字にしてみた
# 公式の解説通り
