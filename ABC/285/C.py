S = input()
N = len(S)

res = 0
add = 26

for i in range(1, N):
    res += add
    add *= 26

num = 0
for i in range(N):
    num *= 26
    num += (ord(S[i]) - ord('A'))

print(res + num + 1)
