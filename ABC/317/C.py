N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A-1].append((B-1, C))
    graph[B-1].append((A-1, C))

ans = 0
for i in range(N):
    stack = [(i, 0, [False]*N)]
    while stack:
        node, length, visited = stack.pop()
        visited[node] = True
        ans = max(ans, length)
        for new_node, edge_length in graph[node]:
            if not visited[new_node]:
                stack.append((new_node, length + edge_length, visited.copy()))

print(ans)
