N = int(input())
SC = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(2):
        if SC[i][1] > 1:
            SC[i][1] -= (SC[i][1] // 2) * 2
            exists = False
            for sc in SC:
                if sc[0] == SC[i][0] * 2:
                    sc[1] += SC[i][1] // 2
                    exists = True
                    break
            if not exists:
                SC.append([SC[i][0] * 2, SC[i][1] // 2])

total = sum(row[1] for row in SC)

print(total)
print(SC)
