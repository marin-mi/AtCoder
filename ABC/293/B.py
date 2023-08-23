N = int(input())
A = list(map(int, input().split()))

B = set()
C = []
cnt = 0
for i in range(len(A)):
    if not i + 1 in B:
        B.add(A[i])

for i in range(1, len(A) + 1):
    if not i in B:
        C.append(i)
        cnt += 1
        
print(cnt)
print(*C)

# Bはリストだと全探索するためセットにする必要がある
# セットなためaddになる