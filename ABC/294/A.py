n = int(input())
a = list(map(int, input().split()))

b = list()
for i in a:
    if i % 2 == 0:
        b.append(i)
print(*b)

# *はアンパック