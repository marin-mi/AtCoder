N, M, X, T, D = map(int, input().split())

if M >= X:
    print(T)
else:
    cnt = X - M
    for i in range(cnt):
        T -= D
    print(T)