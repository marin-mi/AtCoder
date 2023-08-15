N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(K):
    A.pop(0) # A[0]を削除
    A.append(0) # 0を追加
    
print(*A)

# O(NK)かかるため処理が遅くなる