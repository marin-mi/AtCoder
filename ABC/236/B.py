N = int(input())
A = list(map(int, input().split()))

cnt = [0] * N
for a in A:
    cnt[a - 1] += 1

for i in range(N):
    if cnt[i] == 3:
        print(i + 1)
        exit()

# 自力で解いた
