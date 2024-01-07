N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    for j in range(L, R + 1):
        if abs(j - A[i]) <= abs( - A[i]):
            ans.append(j)