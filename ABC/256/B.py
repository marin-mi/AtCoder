N = int(input())
A = list(map(int, input().split()))

P = 0
koma = [0]
for a in A:
    new = [0]
    for x in koma:
        if x + a < 4:
            new.append(x + a)
        else:
            P += 1
    koma = new
print(P)

# sano192参考、読みやすくてわかりやすい
# komaはこまがあるリスト、5行目にマス0にコマを置く
# 7行目で新しいコマの場所
# komaにある全てのコマを移動させる
# 4未満ならばnewにappendする
# 4以上ならばPに1を足す
