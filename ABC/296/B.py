S = [input() for _ in range(8)]

R = [8, 7, 6, 5, 4, 3, 2, 1]
C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(8):
    for j in range(8):
        if S[i][j] == '*':
            print(C[j], R[i], sep = '')
            exit()
            
# 40代からの競プロ日記参考
# 行はrow
# 列はcolumn
# sep = ''で空白空けない