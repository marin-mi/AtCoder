N = int(input())
SC = [tuple(map(int, input().split())) for _ in range(N)]

count = [0] * (max(s for s, c in SC) * 2 + 1)

for s, c in SC:
    count[s] += c

for i in range(len(count)):
    if count[i] >= 2:
        count[i + 1] += count[i] // 2
        count[i] %= 2

print(sum(count))
