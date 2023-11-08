S = list(input())
a, b = map(int, input().split())

S[a - 1], S[b - 1] = S[b - 1], S[a - 1]

print(*S, sep='')

# 自分で解いた
# 要素の入れ替えは4行目の通り
# 1行目が文字列だと4行目の動作ができない
# そのためlistにしておく
# unpackして空白を消す
