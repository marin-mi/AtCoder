N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

for a in A:
    if a <= B[0]:
        X = a
    else:
        break
    
print(X)