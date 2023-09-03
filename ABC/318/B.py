N = int(input())
A = []
B = []
C = []
D = []
for i in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
total = sum([(B[i] - A[i]) * (D[i] - C[i]) for i in range(N)])

for i in range(N):
    for j in range(i+1, N):
        overlap_x = max(0, min(B[i], B[j]) - max(A[i], A[j]))
        overlap_y = max(0, min(D[i], D[j]) - max(C[i], C[j]))
        total -= overlap_x * overlap_y
        
print(total)