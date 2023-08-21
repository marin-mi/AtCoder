S = input()

B = []
K = []
R = []

for i in range(8):
    if S[i] == 'B':
        B.append(i)
    elif S[i] == 'K':
        K.append(i)
    elif S[i] == 'R':
        R.append(i)

if B[0] % 2 != B[1] % 2 and R[0] < K[0] < R[1]:
    print('Yes')
else:
    print('No')
    
# それぞれ別のリストに添字を入れることで何番目かを格納する
# 偶奇は全部で4通りあり、2で割ったあまりが違う時だけ偶奇が違う
# Kaiさんのnote参考にした