N = int(input())
T = input()

x, y = 0, 0
dx, dy = 1, 0

for c in T:
    if c == 'S':
        x, y = x + dx, y + dy
    else:
        dx, dy = dy, -dx

print(x, y)

# KA37RIの回答を参考にした
# 回転する際の法則性
# dxとdyを同時に交換するには同時代入を用いる
