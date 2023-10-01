N, Q = map(int, input().split())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)
S = [list(map(int, input().split())) for _ in range(Q)]

for i in range(Q):
    print(A[S[i][0] - 1][S[i][1]])

# クエリは問い合わせる、訪ねるって意味
# データの問い合わせや要求のこと
