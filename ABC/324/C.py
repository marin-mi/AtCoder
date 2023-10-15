N, T = input().split()
S = [input() for _ in range(int(N))]

K = []
for i in range(int(N)):
    if T == S[i]:
        K.append(i + 1)
    elif len(T) == len(S[i]) + 1:
        for j in range(len(S[i]) + 1):
            if T[:j] + T[j + 1:] == S[i]:
                K.append(i + 1)
    elif len(T) == len(S[i]) - 1:
        for j in range(len(S[i])):
            if S[i][:j] + S[i][j + 1:] == T:
                K.append(i + 1)
    elif len(T) == len(S[i]):
        diff_count = sum([t != u for t, u in zip(T, S[i])])
        if diff_count == 1:
            K.append(i + 1)
print(len(K))
print(*K)
