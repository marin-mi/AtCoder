from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1

ans = 0
for i in d:
    ans += d[i] // 2

print(ans)

# Kaiという人の記事を参考にしている
# defaultdictで色と枚数を紐づける
# 色を全て管理することはできないので、リストはNG
