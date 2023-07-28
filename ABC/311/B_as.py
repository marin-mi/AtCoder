N, D = map(int, input().split())
S = [input() for i in range(N)]

ans = 0
tmp_ans = 0
for i in range(D):
    cnt = 0
    for j in range(N):
        if S[j][i] == 'o':
            cnt += 1
    if cnt == N:
        tmp_ans += 1
    else:
        ans = max(ans, tmp_ans)
        tmp_ans = 0
print(max(ans, tmp_ans))

#二次元配列
#連続する日を数えるのでtmp_ansが必要
#cntは列が全てoか見ている