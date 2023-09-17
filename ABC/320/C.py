M = int(input())
S1 = input()
S2 = input()
S3 = input()

min_time = float('inf')
possible = False

for t1 in range(M):
    for t2 in range(M):
        for t3 in range(M):
            if S1[t1] == S2[t2] == S3[t3]:
                possible = True
                time = max(t1, t2, t3) + 1
                min_time = min(min_time, time)

if possible:
    print(min_time)
else:
    print(-1)
