N = int(input())
S = input()

for i in range(1, N):
    for j in range(N):
        if i + j < N:
            if S[j] == S[j + i]:
                print(j)
                break
        else:
            print(j)
            break

# 40代からの競プロ日記を参考にした
# 4行目は2つの文字の間の距離を1からN - 1まで変化させている
# 5行目はSを順に見ていく
# 7行目で一致したらその時の最大値jを出力する
# 問題の題意が読み取りづらい場合はサンプルを見る