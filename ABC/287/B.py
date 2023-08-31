N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

cnt = 0

for i in range(N):
    for j in range(M):
        if S[i][-3:] == T[j]:
            cnt += 1
            break

print(cnt)

# Sは二次元配列なので9行目のような表記になる
# Tのリストに1つでも一致すればよいので1つでも一致したらbreakする