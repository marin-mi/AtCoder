a, b, c, x = map(int, input().split())

ans = 1
if x <= a:
    ans = a / a
elif a + 1 <= x <= b:
    ans = c / (b - a)
else:
    ans = 0
print(ans)
