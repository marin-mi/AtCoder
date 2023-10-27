import math


def solve(N, X, F, S):
    dp = [[float('inf')] * (X + 1) for _ in range(N + 1)]
    dp[0][X] = 0

    for i in range(N + 1):
        for j in range(X + 1):
            if dp[i][j] == float('inf'):
                continue

            next_speed = max(j - F, 0)
            next_lines = min(N, i + j)
            dp[next_lines][next_speed] = min(
                dp[next_lines][next_speed], dp[i][j] + 1)

            next_speed_sleep = min(X, j + S)
            dp[i][next_speed_sleep] = min(
                dp[i][next_speed_sleep], dp[i][j] + 3)
    return min(dp[N])


N, X, F, S = map(int, input().split())
ans = solve(N, X, F, S)
print(ans)
