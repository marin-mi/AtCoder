N = int(input())
ice = []
for i in range(N):
    F, S = map(int, input().split())
    ice.append((F, S))

ice.sort(key=lambda x: x[1], reverse=True)

s = ice[0][1]

max_ = 0
for i in range(1, N):
    t = ice[i][1]
    if ice[0][0] != ice[i][0]:
        max_ = max(max_, s + t)
    else:
        max_ = max(max_, s + t // 2)

print(max_)
