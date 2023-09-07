def isPrime(N):
    limit = int(N ** 0.5)
    for i in range(2, limit + 1):
        if N % i == 0:
            return False
    return True


# 入力
Q = int(input())
X = [None] * Q
for i in range(Q):
    X[i] = int(input())

# 出力
for i in range(Q):
    flag = isPrime(X[i])
    if flag:
        print('Yes')
    else:
        print('No')
