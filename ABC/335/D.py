N = int(input())

grid = [[0 for _ in range(N)] for _ in range(N)]

takahashi_pos = (N // 2, N // 2)
grid[takahashi_pos[0]][takahashi_pos[1]] = 'T'

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = takahashi_pos
part_num = 1
for step_size in range(1, N, 2):
    for d in range(4):
        for _ in range(step_size + (d > 1)):
            x += dx[d]
            y += dy[d]
            if 0 <= x < N and 0 <= y < N:
                grid[x][y] = part_num
                part_num += 1
        if part_num > N*N - 1:
            break
    if part_num > N*N - 1:
        break

for row in grid:
    print(' '.join(map(str, row)))
