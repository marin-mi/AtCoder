N = int(input())

yaku = []
for i in range(1, 10):
    if N % i == 0:
        yaku.append(i)
S = ''
for i in range(N + 1):
    val = []
    for j in yaku:
        if i % (N // j) == 0:
            val.append(j)
    if val:
        S += str(min(val))
    else:
        S += '-'
print(S)
