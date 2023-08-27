N = int(input())
diffs = []
total_seats = 0
for _ in range(N):
    X, Y = map(int, input().split())
    diffs.append(2*X + Y)
    total_seats -= X

diffs.sort(reverse=True)

ans = 0
for diff in diffs:
    if total_seats <= 0:
        break
    total_seats += diff
    ans += 1

print(ans)