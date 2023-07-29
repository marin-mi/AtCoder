N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

price = P

for i in D:
    if Q + i < price:
        price = Q + i

print(price)