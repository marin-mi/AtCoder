N, D = map(int, input().split())
S = [input() for _ in range(N)]

all_free = ''.join('o' if all(s[d] == 'o' for s in S) else 'x' for d in range(D))

max_days = max(len(days) for days in all_free.split('x'))

print(max_days)

