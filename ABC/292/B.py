N, Q = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(Q)]

card = [0] * N
for event in l:
    a, x = event[0], event[1]
    if a == 1:
        card[x - 1] += 1
    elif a == 2:
        card[x - 1] += 2
    elif a == 3:
        if card[x - 1] >= 2:
            print('Yes')
        else:
            print('No')
            
# TechMath Projectさんの記事を参考にした
# 2行目で質問がQ回なのにrange(N)としていたためエラーが出た
# 要素は横に保存
# cardというリストで受けたカードの点数をカウントしている
# 5,6行目は数列ある時のfor文のスマートな書き方なので覚える