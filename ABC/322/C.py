N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(len(A)):
    if i == 0:
        cnt = A[i] - 1
    else:
        cnt = A[i] - A[i - 1] - 1
    while cnt >= 0:
        print(cnt)
        cnt -= 1

# 出力例から解法導出した
