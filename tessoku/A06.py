N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = []
R = []
for _ in range(Q):
    Li, Ri = map(int, input().split())
    L.append(Li)
    R.append(Ri)

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]
for j in range(Q):
    print(S[R[j]] - S[L[j] - 1])
