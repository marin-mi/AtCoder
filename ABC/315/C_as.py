N = int(input())
G = [[] for _ in range(N)]
for _ in range(N):
    f, s = map(int, input().split())
    G[f - 1].append(s)

for i in range(N):
    G[i].sort(reverse = True)
    
ans = 0

# 同じアイスクリームの満足度
for i in range(N):
    if len(G[i]) >= 2:
        ans = max(ans, G[i][0] + G[i][1] // 2)
        
# 違うアイスクリームの満足度       
top = []
for i in range(N):
    if len(G[i]) >= 1:
        top.append(G[i][0])
top.sort(reverse = True)
ans = max(ans, sum(top[:2]))

print(ans)

# AtCoderでは実行時間が2秒に設定されており、これはO(10^8)が限界である
# 今回はN個の中から2つを選ぶので、for文2重ループ
# しかし、それではO(N^2)となり、今回のNの最大値が10^5なためO(10^10)となりTLEとなる
# 計算量を削減するために二次元配列を使用する
# hyouchunという人の記事を参考にした
# 解説と同じ考え方