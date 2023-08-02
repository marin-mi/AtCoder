#探索がメインの解法

N = int(input())

#答えの候補である、0, 5, ... , 100を全てチェックしてNとの差が一番小さいものを出力
ans = 100
for i in range(0, 101, 5):
    if abs(N - i) < abs(N - ans):
        ans = i

print(ans)