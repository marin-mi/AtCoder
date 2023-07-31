N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

target = [
    '###.?????', 
    '###.?????', 
    '###.?????',
    '....?????',
    '?????????',
    '?????....',
    '?????.###',
    '?????.###',
    '?????.###'
]

for i in range(N - 8):
    for j in range(M - 8):
        flag = True
        for x in range(9):
            for y in range(9):
                if target[x][y] != '?' and S[i + x][j + y] != target[x][y]:
                    flag = False
        
        if flag:
            print(i + 1, j + 1)
            
                    
