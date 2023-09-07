N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    if not S[i][0] in 'HDCS':
        print('No')
        exit()
    elif not S[i][1] in 'A23456789TJQK':
        print('No')
        exit()
    elif len(set(S)) != N:
        print('No')
        exit()
print('Yes')

# 綺麗な書き方
