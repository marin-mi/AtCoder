N = int(input())
G = [[] for _ in range(N)]
for _ in range(N):
    f, s = map(int, input().split())
    G[f - 1].append(s)

print(G)
