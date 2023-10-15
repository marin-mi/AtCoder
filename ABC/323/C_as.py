N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

score = [0] * N
for i in range(N):
    for j in range(M):
        if S[i][j] == 'o':
            score[i] += A[j]
    score[i] += i + 1

for i in range(N):
    max_other_score = max(score[:i] + score[i+1:])
    remaining_problems = [A[j] for j in range(M) if S[i][j] == 'x']
    remaining_problems.sort(reverse=True)
    needed_score = max_other_score - score[i] + 1
    solved_problems = 0
    while needed_score > 0 and solved_problems < len(remaining_problems):
        needed_score -= remaining_problems[solved_problems]
        solved_problems += 1
    print(solved_problems)
