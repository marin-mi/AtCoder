N = int(input())
G = [[0 for _ in range(100)]for _ in range(100)]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    for x in range(a, b):
        for y in range(c, d):
            G[x][y] = 1
            
ans = 0
for i in range(100):
    ans += sum(G[i])

print(ans)

# 100 * 100のグリッド(マス)に0をいれる
# x軸はa,b、y軸はc,dの範囲でマスを1にする
# xを1つずつ見ていき最終的に何個1があるか数える