A = list(map(int, input().split()))

if len(set(A)) == 2:
    if A.count(A[0]) == 2 or A.count(A[0]) == 3:
        print('Yes')
        exit()
print('No')

# 260Aの応用
# mgumiさんのを参考にした
# 条件としては長さが2でカウントが2か3のとき