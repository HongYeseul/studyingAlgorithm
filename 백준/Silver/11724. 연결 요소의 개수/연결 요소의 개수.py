import sys
sys.setrecursionlimit(999999)

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

visited = [0 for _ in range(N+1)]


def recur(node):
    visited[node] = 1

    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        recur(nxt)

cnt = 0
for node in range(1, N+1):
    if visited[node] == 0:
        recur(node)
        cnt += 1

    if sum(visited) == N:
        break


# print(visited)
print(cnt)