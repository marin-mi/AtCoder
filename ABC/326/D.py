N = int(input())
R = input()
C = input()

G = [['.' for _ in range(N)] for _ in range(N)]

for i in range(N):
    G[i][i] = R[i]
    G[i][N-1-i] = C[i]

for i in range(N):
    if G[i][0] != R[i]:
        print("No")
        exit()

for i in range(N):
    if G[0][i] != C[i]:
        print("No")
        exit()

print("Yes")
for row in G:
    print(''.join(row))
