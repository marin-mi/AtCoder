N, H, X = map(int, input().split())
P = list(map(int, input().split()))

hp = H
cnt = 0
for i in range(N):
    cnt += 1
    if hp + P[i] >= X:
        print(cnt)
        exit()