N = int(input())
H = list(map(int, input().split()))

tmp = H[0]
for i in range(N - 1):
    if H[i] < H[i + 1]:
        tmp = H[i + 1]
    else:
        break
print(tmp)

# 自分で解いた
