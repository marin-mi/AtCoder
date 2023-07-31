L, R = map(int, input().split())
S = input()

rev = list(S[L - 1:R])
rev.reverse()
result = ''.join(rev)
ans = S[:L - 1] + result + S[R:]
print(ans)