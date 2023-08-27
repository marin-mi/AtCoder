N = int(input())
ice = []
for i in range(N):
    F, S = map(int, input().split())
    ice.append((F, S))

print(F)


# AtCoderでは実行時間が2秒に設定されており、これはO(10^8)が限界である
# 今回はN個の中から2つを選ぶので、for文2重ループ
# しかし、それではO(N^2)となり、今回のNの最大値が10^5なためO(10^10)となりTLEとなる
# qiitaの記事更新する(縦型の標準入出力の新しいやり方)