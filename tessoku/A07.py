D = int(input())
N = int(input())
L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

B = [0] * (D + 2)
for i in range(N):
    B[L[i]] += 1
    B[R[i] + 1] -= 1

ans = [0] * (D + 2)
for i in range(1, D + 1):
    ans[i] = ans[i - 1] + B[i]
    print(ans[i])

# 出席者数の前日比を記録した配列Bを用意する
# 2-4日目まで出席だと2日目に1増えて、4日目に1減る
# 累計来場者数が配列ans(累積和)、1日目から始まる
# D + 2なのは、2日なら0, 1, 2, 3とするため