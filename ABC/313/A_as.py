n = int(input())
p = list(map(int, input().split()))

m = 0
for i in range(1, n):
    m = max(m, p[i])
ans = max(0, m + 1 - p[0])
print(ans)

# 1からn-1まで
# maxの求め方
# max(0, )で負の値にならないようにしている