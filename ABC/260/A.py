S = input()

for s in S:
    if S.count(s) == 1:
        print(s)
        exit()
print(-1)

# リストSの中でsを探索する
# Sの中でsが1つなら1を出力してそれ以外なら-1を出力する
# tostartwithさんの答えを参考にした