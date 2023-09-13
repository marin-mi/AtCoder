# 入力
N = int(input())
T = [None] * N
A = [None] * N
for i in range(N):
    T[i], A[i] = input().split()
    A[i] = int(A[i])

# 出力
ans = 0
for i in range(N):
    if T[i] == '+':
        ans += A[i]
    elif T[i] == '-':
        ans -= A[i]
    elif T[i] == '*':
        ans *= A[i]
    # 引き算で答えが0未満になった時
    if ans < 0:
        ans += 10000
    # 余りをとる
    ans %= 10000
    print(ans)
