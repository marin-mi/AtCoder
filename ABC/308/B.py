N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

ans = 0
for c in C:
    price = P[0]
    for j in range(M):
        if c == D[j]:
            price = P[j + 1]
            break
    ans += price

print(ans)

# CとDはint型でないのでmapはいらない
# CとDが一致しないときってすると一致しない時全てでP[0]が追加されてしまう
# Cの要素が一致する時だけpriceを変更してfor文を抜け出す
# for文を抜けた後にpriceを追加する
