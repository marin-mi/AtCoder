N = int(input())
A = list(map(int, input().split()))

visited = [-1] * N
current = 0
path = []

while visited[current] == -1:
    visited[current] = len(path)
    path.append(current)
    current = A[current] - 1

cycle = path[visited[current]:]
print(len(cycle))
for v in cycle:
    print(v + 1)