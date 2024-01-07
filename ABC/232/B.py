S = input()
T = input()

ans = set()
for i in range(len(S)):
    k = (ord(T[i]) - ord(S[i]) + 26) % 26
    ans.add(k)

if len(ans) == 1:
    print('Yes')
else:
    print('No')

# print(ord('a'))
# print(chr(97))
# @uniTMの解説を参考にした
# Unicodeと言われる集合体によって文字を数字に変換できる
# ここで割り振られる番号をコードポイントという
# 文字列は一文字のみ
# kによってTとSの差を調べている
# zとaの時、-25になって距離が正しくないので、26を足して26で割ったあまりを求めている
# 全ての距離の差をansに入力
# 全ての距離の差が等しい時、つまり長さが1になる時Yesにする
# orderで文字の順序を意味する
# chrはcharactorで文字を意味する
# あまりは必ず正の数になるので26を足す必要はない
