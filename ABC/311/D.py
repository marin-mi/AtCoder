N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    S[x][y] = '#'
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and S[nx][ny] == '.':
            dfs(nx, ny)

for i in range(N):
    for j in range(M):
        if S[i][j] == '.':
            start = (i, j)
            break

dfs(*start)

print(sum(row.count('.') for row in S))