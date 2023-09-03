N, D, P = map(int, input().split())
F = list(map(int, input().split()))

base = P // D
cnt = 0
over = 0
for i in range(N):
    if F[i] >= base:
        cnt += 1
        over += F[i]
if cnt > 0:
    hiku = over // P
    F.sort(reverse=True)
    S = F[D * hiku:]
    ans = sum(S) + hiku * P
else:
    ans = sum(F)

if cnt > 0:
    kake = cnt // D
    if cnt % D != 0:
        kake += 1

    if kake * P < ans:
        ans = kake * P

print(ans)
