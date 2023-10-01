N, M = map(int, input().split())
P, C, F = [], [], []
for _ in range(N):
    L = list(map(int, input().split()))
    P.append(L[0])
    C.append(L[1])
    F.append(set(L[2:]))

flag = False
for i in range(N):
    for j in range(N):
        if P[i] >= P[j] and F[j].issuperset(F[i]) \
                and (P[i] > P[j] or len(F[j]) > len(F[i])):
            flag = True
if flag:
    print('Yes')
else:
    print('No')

# 公式の解説参考にしている
# 7行目はsetにする、あとは愚直にするだけ
# いずスーパーセットで上位集合か判定する
