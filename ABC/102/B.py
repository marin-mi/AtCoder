N = int(input())
A = list(map(int, input().split()))

dif = abs(max(A) - min(A))
print(dif)