N = int(input())
A = []
for _ in range(N):
    c = int(input())
    a = list(map(int, input().split()))
    A.append(a)
X = int(input())

ans = []
cnt = 37
for i in range(N):
    if X in A[i]:
        if cnt > len(A[i]):
            ans = [i + 1]
            cnt = len(A[i])
        elif cnt == len(A[i]):
            ans.append(i + 1)

print(len(ans))
print(*ans)

# 14行目でリストを初期化する
# cntは37の最大値にしておく
