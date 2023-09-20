n = int(input())
p = list(map(int, input().split()))

m = 0
for i in range(1, n):
    m = max(m, p[i])
ans = max(0, m + 1 - p[0])
print(ans)

# 公式の解説参考にしている
# 5行目はpを0番目を抜いて、1からn-1(最後)まで見ていっている
# max(0, )で負の値にならないようにしている
