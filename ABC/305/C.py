H, W = map(int, input().split())
S = [input() for _ in range(H)]

min_i, max_i = 1000, -1
min_j, max_j = 1000, -1

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            min_i = min(min_i, i)
            max_i = max(max_i, i)
            min_j = min(min_j, j)
            max_j = max(max_j, j)

for i in range(min_i, max_i + 1):
    for j in range(min_j, max_j + 1):
        if S[i][j] == '.':
            print(i + 1, j + 1)

# hyouchun参考
# iとjの最小値、最大値を入れる変数を用意する
# 最小値なら最大に、最大値なら最小の取らない値を初期値にする
# #があったらiとどちらが最小か比較すす
# .があったときにprintする
