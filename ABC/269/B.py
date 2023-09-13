S = [input() for _ in range(10)]

A = 10
B = 1
C = 10
D = 1
for i in range(10):
    for j in range(10):
        if S[i][j] == '#':
            A = min(A, i + 1)
            B = max(A, i + 1)
            C = min(C, j + 1)
            D = max(C, j + 1)
print(A, B)
print(C, D)

#  aPNJ777さんの回答を参考にした
# iは行なのでAとB
# jは列なのでCとD
# Aは最小値をとるため最も大きい値にする
# 逆もまた然り
