N = int(input())
S = [input() for _ in range(N)]

if S.count('For') > len(S) / 2:
    print('Yes')
else:
    print('No')
    
# 4行目はif S.count('For') > N // 2:の方がいい