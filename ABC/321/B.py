N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

mid = sum(A[1:-1])

for i in range(0, 101):
    tmp = mid
    if i <= min(A):
        tmp += min(A)
    elif min(A) <= i <= max(A):
        tmp += i
    else:
        tmp += max(A)
    if tmp >= X:
        print(i)
        exit()
print(-1)

# sugipamoの回答も参考になる
# 昂生の回答を参考にした
# 全探索している
# 最終ラウンドのスコアiがmin(A)より小さい時、min(A)とmax(A)の間、max(A)より大きい時の3つに場合分けする
# iは0から100まで
# それぞれの場合分けに応じてtmp(mid)の値を変更する
# 問題文通り、Xを超えた時にiを出力してexit()でプログラムを強制終了する
# 0~100の範囲で条件を満たすiが見つからなかった場合-1を出力する
