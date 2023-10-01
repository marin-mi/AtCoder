X, Y = [], []
for _ in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

a, b = 0, 0
for i in range(3):
    if X.count(X[i]) == 1:
        a = X[i]
    if Y.count(Y[i]) == 1:
        b = Y[i]
print(a, b)

# リストで管理
