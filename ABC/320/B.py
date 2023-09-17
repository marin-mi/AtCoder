S = input()

N = len(S)
ans = 0
for i in range(N):
    for j in range(i, N + 1):
        T = S[i:j]
        if T == T[::-1]:
            ans = max(ans, len(T))
print(ans)

# 5行目は回文の最初の文字
# 6行目は回文の最後の文字
