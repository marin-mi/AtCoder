N, T = map(int, input().split())
A = list(map(int, input().split()))

tmp = T % sum(A)
for i in range(N):
    if tmp - A[i] < 0:
        print(i + 1, tmp)
        exit()
    else:
        tmp -= A[i]

# 愚直に行うとO(T)でTLEとなるため合計値で割ったあまりを調べる
# 周期性を利用するとO(N)で解ける
