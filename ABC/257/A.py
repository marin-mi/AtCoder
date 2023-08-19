N, X = map(int, input().split())

S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if X % N == 0:
    ans = X // N
else:
    ans = (X // N) + 1
print(S[ans - 1])