N, M, P = map(int, input().split())

cnt = 0
for i in range(M, N + 1):
    M += P
    cnt += 1
    if M > N:
        break
print(cnt)
