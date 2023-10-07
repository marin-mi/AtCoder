H, W = map(int, input().split())
S = [input() for _ in range(H)]

pieces = []
for i in range(H):
    for j in range(W):
        if S[i][j] == 'o':
            pieces.append((i, j))
a, b = pieces[0]
c, d = pieces[1]
print(abs(a - c) + abs(b - d))

# 公式の解説
# 8行目以降のやり方覚える
