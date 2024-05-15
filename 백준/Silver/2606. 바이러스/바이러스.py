import sys

nodeN = int(sys.stdin.readline())
edgeN = int(sys.stdin.readline())
graph = [[] for _ in range(nodeN+1)]
for _ in range(edgeN):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(nodeN+1)]
cnt = 0

def dfs(node):
    global cnt
    visited[node] = 1
    cnt += 1

    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        dfs(nxt)

dfs(1)
print(cnt -1)