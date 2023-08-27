N = int(input())
moun = []
for i in range(N):
    S, T = input().split()
    moun.append([S, int(T)])

moun.sort(reverse = True, key = lambda x:x[1])

print(moun[1][0])

# youtube、緑になるための典型50講の二次元配列とソートからの問題
# 二次元配列の問題
# reverse = Trueで大きい順にする
# key = lambda x:x[1]で二次元配列の2列目を指定している
# 2番目に高い山の名前なので1行目の0列目を出力する
# 公式の解説では、S Tで受け取りT Sの順にappendしているのでそのままsortできる