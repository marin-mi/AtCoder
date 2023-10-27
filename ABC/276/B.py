N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b)
    G[b - 1].append(a)

for i, name in enumerate(G):
    name.sort()
    print(len(name), *name)

# アルゴ式のグラフと公式の解説を参考
# グラフときたらこの形を覚える
# a→bの有向グラフはG[a].append(b)と書く
# 無向グラフなのでその反対もする
# 今回のグラフは1indexなので-1する
# enumerateはindexと要素
