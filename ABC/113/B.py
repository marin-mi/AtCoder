N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

nearest = 10 ** 10
ans = 1
tmp = 0

for i, Hi in enumerate(H, 1):
    tmp = T - Hi * 0.006
    if abs(A - tmp) < nearest:
        ans = i
        nearest = abs(A - tmp)
        
print(ans)
