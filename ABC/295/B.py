R, C = map(int, input().split())
B = [input() for _ in range(R)]

for i in range(R):
    for j in range(C):
        x = B[i][j]
        for m in range(R):
            for n in range(C):
                if B[m][n].isdigit():
                    p = int(B[m][n])
                else:
                    p = -1
                if abs(i - m) + abs(j - n) <= p:
                    x = '.'
        print(x, end='')
    print()

# 公式の解説を参考にした
# isdigitで数字かどうか判定し、Trueなら文字列を整数型に変換する
# マンハッタン距離が爆弾以下なら.にする
# 15行目は改行せずに次の値を出力する
# 16行目は悪行の最後に改行を出力する
