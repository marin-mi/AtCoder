N = int(input())
A = list(map(int, input().split()))

count = 0
flag = True

while True:
    for i in range(N):
        if A[i] % 2 != 0:
            flag = False
    if flag is False:
        break
    for i in range(N):
        A[i] = A[i] // 2
    count += 1
    
print(count)