X, Y, N = map(int, input().split())

if Y > 3 * X:
    print(N * X)
    exit()
if N % 3 == 0:
    ans = N // 3 * Y
    print(ans)
elif N % 3 == 1:
    ans = N // 3 * Y + X
    print(ans)
else:
    ans = N // 3 * Y + 2 * X
    print(ans)