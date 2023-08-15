N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(K):
    A = A[1:] + [0]
    
print(*A)

# リストの1から最後までを切り出し、最後に0を追加する
# これをK回繰り返す