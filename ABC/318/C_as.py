N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)

for left in range(0, N, D):
    right = min(left + D, N)
    cost = sum(F[left:right])
    if cost > P:
        for i in range(left, right):
            F[i] = 0
        F[left] = P
    else:
        break

ans = sum(F)
print(ans)

# hyouchunの記事を参考にした
# 運賃を高い順にsortし、D日ずつの合計を計算する
# 損益をP以下か判定する
