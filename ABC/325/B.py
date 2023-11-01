N = int(input())
cnt = [0 for _ in range(24)]
for _ in range(N):
    w, x = map(int, input().split())
    cnt[x] += w

ans = 0
for i in range(24):
    sum = 0
    for j in range(9):
        sum += cnt[(i + j) % 24]
    ans = max(ans, sum)

print(ans)

# 公式解説
# cntで24時間の人数を格納する
# 11行目がよくわからん
