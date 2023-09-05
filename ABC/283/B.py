N = int(input())
A = list(map(int, input().split()))
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

for i in range(Q):
    if query[i][0] == 1:
        A[query[i][1] - 1] = query[i][2]
    elif query[i][0] == 2:
        print(A[query[i][1] - 1])

# Aのリストが1から始まっていることに注意
