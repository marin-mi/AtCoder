N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for l in L:
    if A[l - 1] == N:
        continue
    if A[l - 1] + 1 in A:
        continue
    else:
        A[l - 1] += 1
print(*A)

# ryomac1の回答を参考にした
# 0indexなので6行目で-1する
# あるかどうかは8行目のようにかける
# 1マス動かすのは11行目のようにかける
# passはそれ以降の処理行う、continueはそれ以降の処理行わない
