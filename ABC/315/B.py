M = int(input())
D = list(map(int, input().split()))

day = (sum(D) + 1) // 2
day_ = 0
a = 0
b = 0

for i in range(M):
    day_ += D[i]
    if day <= day_:
        b = day - (day_ - D[i])
        a = i + 1
        print(a, b)
        exit()