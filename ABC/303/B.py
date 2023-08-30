N , M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(M)]

pair = set()
for row in a:
    for i in range(N - 1):
        x, y = row[i], row[i + 1]
        pair.add((x, y))
        pair.add((y, x))
        
ans = N * (N - 1) // 2 - len(pair) // 2
print(ans)

# hyouchunの記事を参考にした
# 隣り合ったペアをpairというセットに入れていく
# 左右逆でも対応できるように9行目のようにしてsetに入れておく
# n人から2人を選ぶ組み合わせはn * (n - 1) / 2
# 11行目は左右で重複しているため2で割る