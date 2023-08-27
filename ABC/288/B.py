N, K = map(int, input().split())
S = [input() for _ in range(N)]

A = list(S[:K])
A.sort()
for i in range(len(A)):
    print(A[i])
    
# 辞書順と言われたらsort()と脊髄反射的に出るようにする
# 4行目の書き方忘れない