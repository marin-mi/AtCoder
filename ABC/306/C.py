N = int(input())
A = list(map(int, input().split()))

cnt = [0 for _ in range(N + 1)]
ans = []
for a in A:
    cnt[a] += 1
    if cnt[a] == 2:
        ans.append(a)
print(*ans)

# 公式の解説
# 4行目は3 * NじゃなくてN + 1でok
