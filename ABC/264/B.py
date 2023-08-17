R, C = map(int, input().split())

grid = [
    '###############',
    '#.............#',
    '#.###########.#',
    '#.#.........#.#',
    '#.#.#######.#.#',
    '#.#.#.....#.#.#',
    '#.#.#.###.#.#.#',
    '#.#.#.#.#.#.#.#',
    '#.#.#.###.#.#.#',
    '#.#.#.....#.#.#',
    '#.#.#######.#.#',
    '#.#.........#.#',
    '#.###########.#',
    '#.............#',
    '###############'
]

if grid[R - 1][C - 1] == '#':
    print('black')
else:
    print('white')
    
# 312Bに似てる
# gridには,を忘れない
# 埋め込む方が楽
# チェビシェフ距離でも解ける