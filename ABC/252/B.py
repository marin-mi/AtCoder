N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

tabe = []
for i in range(N):
    if A[i] == max(A):
        tabe.append(i + 1)
ans = set(tabe) & set(B)
if len(ans) > 0:
    print('Yes')
else:
    print('No')

# setを使ってリストの共通部分があるか調べてる
