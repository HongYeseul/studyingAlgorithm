#2606 바이러스 (https://www.acmicpc.net/problem/2606)

N = int(input())
M = int(input())


graph = [ [] for _ in range(N+1)]
visited = [ 0 for _ in range(N+1) ]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def DFS(node):
    visited[node] = 1

    for next in graph[node]:
        if visited[next] == 1: continue
        DFS(next)

DFS(1)
print(sum(visited)-1)