N = int(input())
cnt = [0] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    cnt[a - 1] += 1
    cnt[b - 1] += 1

for i in range(N):
    if cnt[i] == N - 1:
        print('Yes')
        exit()
print('No')

# 公式の解説
# グラフ