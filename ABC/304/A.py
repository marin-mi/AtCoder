#プログラミングの広場参照
N = int(input())
S = []
A = []
for i in range(N):
    si, ai = input().split()
    S.append(si)
    A.append(int(ai))

minA = 10 ** 9 + 1
min_index = -1
for i in range(N):
    if A[i] < minA:
        minA = A[i]
        min_index = i
        
for i in range(N):
    print(S[(min_index + i) % N])