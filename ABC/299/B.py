N, T = map(int, input().split())
C = [0] + list(map(int, input().split()))
R = [0] + list(map(int, input().split()))

tmax = (-1, -1)
lmax = (-1, -1)

for i in range(1, N + 1):
    if C[i] == T:
        tmax = max(tmax, (R[i], i))
    if C[i] == C[1]:
        lmax = max(lmax, (R[i], i))

if tmax[0] != -1:
    print(tmax[1])
else:
    print(lmax[1])

# タプルの比較は1つ目の要素から行われる
# tmaxが変更されている、つまり、Tが存在したら最大値を出力する
