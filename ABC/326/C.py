N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = 0
j = 0
for i in range(N):
    while j < N and A[j] < A[i] + M:
        j += 1
    count = j - i
    ans = max(ans, count)

print(ans)
