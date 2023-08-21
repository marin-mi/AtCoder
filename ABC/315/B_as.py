M = int(input())
D = list(map(int, input().split()))

mid = (sum(D) + 1) // 2

for i, d in enumerate(D, 1):
    if mid - d <= 0:
        print(i, mid)
        exit()
    else:
        mid -= d

# スマートな解答
# dはi月の日数を表している
# 40代からの競プロ日記参考にした