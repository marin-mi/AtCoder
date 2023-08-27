N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A-1].append((B-1, C))
    graph[B-1].append((A-1, C))
    
print(graph)