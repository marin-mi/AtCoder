N = int(input())

for i in range(0, N + 1):
    for j in range(0, N + 1):
        for k in range(0, N + 1):
            if k <= N - i - j and k >= 0:
                print(i, j, k)
