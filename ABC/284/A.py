N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    print(S[- (i + 1)])
    
# -(i+1)で後ろからになる
# -1で一番うしろのリスト