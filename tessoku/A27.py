def GCD(A, B):
    while A >= 1 and B >= 1:
        if A >= B:
            A = A % B
        else:
            B = B % A
    if A >= 1:
        return A
    return B


# 入力
A, B = map(int, input().split())

# 出力
print(GCD(A, B))
