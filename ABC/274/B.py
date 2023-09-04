H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

cnt = [0] * W
for i in range(H):
    for j in range(W):
        if C[i][j] == '#':
            cnt[j] += 1

print(*cnt)

# 列をカウントする方法
