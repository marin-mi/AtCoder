N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        xi, yi = xy[i]
        xj, yj = xy[j]
        d2 = (xi - xj) ** 2 + (yi - yj) ** 2
        ans = max(d2, ans)
print(ans ** 0.5)


# KA37RIの解答を参考
# O(N ** 2)でも間に合う
# 7行目の表記を覚える
# 3つの中から2つ選ぶ組み合わせは3C2
# 3! / 2!(3 - 2)!を計算すると組み合わせの数が出る
# N個の中から2個選ぶ組合せは N(N - 1) / 2で求まる
# 計算量は多くて10 ** 4
