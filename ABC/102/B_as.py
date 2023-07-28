N = int(input())
A = list(map(int, input().split()))

max_A = A[0]
min_A = A[0]

for a in A:
    if a > max_A:
        max_A = a
    if a < min_A:
        min_A = a

print(max_A - min_A)