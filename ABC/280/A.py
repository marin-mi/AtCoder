H, W = map(int, input().split())
S = [input() for _ in range(H)]

count = sum(row.count('#') for row in S)

print(count)