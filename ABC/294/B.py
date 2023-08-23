H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
B = []
for i in range(H):
    for j in range(W):
        if A[i][j] == 0:
            B += '.'
        else:
            B += alf[A[i][j] - 1]
    print(''.join(B))
    B = []

# 12行目は*すると空白が含まれるのでjoinでリストを文字列にする