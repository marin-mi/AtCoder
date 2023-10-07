N = int(input())
S = list(input())

lef = True
for i in range(N):
    if lef and S[i] == ',':
        S[i] = '.'
    if S[i] == '"':
        lef = not lef
print(''.join(S))

# 括られた文字の条件 = その文字の左に"が奇数個存在する
# 9行目でflagの真理値を反転させる
# FとTを繰り返す
# 文字列を指定して変更することはできないのでlist
# リストの要素を繋げるためにjoin
