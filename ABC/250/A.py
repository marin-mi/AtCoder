H, W = map(int, input().split())
R, C = map(int, input().split())

cnt = 4
if R == 1:
    cnt -= 1
if R == H:
    cnt -= 1
if C == 1:
    cnt -= 1
if C == W:
    cnt -= 1

print(cnt)

# 7行目をelifにすると5行目が真の時評価されない
# そのためifにする必要がある
# 自己流
