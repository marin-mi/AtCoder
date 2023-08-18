N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
L = []
R = []
for _ in range(Q):
    Li, Ri = map(int, input().split())
    L.append(Li)
    R.append(Ri)

S = [0] * (N + 1)
for i in range(1, N + 1):
    S[i] = S[i - 1] + A[i]
for j in range(Q):
    print(S[R[j]] - S[L[j] - 1])

# 12行目と14行目は表を作って考える
# 10行目は0が横にN + 1個入ったリストが作成される
# 2~4日目だと4-2ではなく、4-(2-1)をする
# 11,12行目の累計来場者数は0日目が必要ないので1, N + 1
# それぞれの来場者数のリストは0日目が0なので[0]を追加する