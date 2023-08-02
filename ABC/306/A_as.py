#文字列を使った解法(教えてもらった)

N = int(input())
S = input()

ans = ''
for i in range(N):
    ans += S[i] * 2

print(ans)