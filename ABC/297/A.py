n, d = map(int, input().split())
t = list(map(int, input().split()))

for i in range(1, n):
    if t[i] - t[i - 1] <= d:
        print(t[i])
        exit()
print(-1)

# N = 5のとき
# range(1, N) 1, 2, 3, 4
# range(N)    0, 1, 2, 3, 4

# リストか、range(N)かrange(1, N)