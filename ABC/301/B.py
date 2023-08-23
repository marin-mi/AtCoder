N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(len(A) - 1):
    if A[i] <= A[i + 1]:
        B += list(range(A[i], A[i + 1]))
    elif A[i] > A[i + 1]:
        B += list(range(A[i], A[i + 1], -1))
        
B.append(A[-1])
print(*B)

# 7行目はA[i + 1]を含まない
# 11行目でAの最後の要素を追加している
# 公式の解説を参考にした
# 計算量O(M)