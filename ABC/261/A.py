A = list(map(int, input().split()))

Rmin = min(A[1], A[3])
Lmax = max(A[0], A[2])

if Rmin - Lmax < 0:
    print(0)
else:
    print(Rmin - Lmax)
    
# いくつかパターンを作って考える
# 重なってるとこの長さは、右端は2直線の右端それぞれの値が小さい方
# 左端は2直線の左端それぞれの値が大きい方で決まる