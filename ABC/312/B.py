N, M = map(int, input().split())
S = [list(input()) for i in range(N)]

for i in range(N - 8):
    for j in range(M - 8):
        for di in range(9):
            for dj in range(9):
                print(S[:3][:3])
                if S[:3][:3] == '#' and S[6:][6:] == '#' and S[3][0:4] == '.' \
                    and S[0:4][3] == '.' and S[5][5:] == '.' and S[5:][5] == '.':
                    print(i + 1, j + 1)