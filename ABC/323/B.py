N = int(input())
S = [input() for _ in range(N)]

win_cnt = [0] * N
for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            win_cnt[i] += 1

ranking = sorted([(count, i) for i, count in enumerate(win_cnt)], key=lambda x: (-x[0], x[1]))

for _, player_num in ranking:
    print(player_num + 1, end=" ")
