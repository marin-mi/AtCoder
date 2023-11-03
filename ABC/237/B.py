def transpose(a):
    """転置行列を求める

    Args:
        a (list): h行w列の行列
    """
    h = len(a)
    w = len(a[0])

    b = [[0 for _ in range(h)] for _ in range(w)]
    for i in range(w):
        for j in range(h):
            b[i][j] = a[j][i]
    return b


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = transpose(A)
for b in B:
    print(*b)
