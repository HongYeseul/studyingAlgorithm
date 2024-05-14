import sys
from collections import deque

def dfs(node):
    print(node, end=" ")
    visitedDFS[node] = 1

    for nxt in graph[node]:
        if visitedDFS[nxt] == 1:
            continue
        dfs(nxt)

def bfs(node):
    queue = deque([node])
    visitedBFS[node] = 1

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for i in graph[node]:
            if visitedBFS[i] == 0:
                visitedBFS[i] = 1
                queue.append(i)

N, M, startNode = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

# 정렬
for arr in graph:
    arr.sort()

# dfs
visitedDFS = [0 for _ in range(N+1)]
dfs(startNode)
print()

# bfs
visitedBFS = [0 for _ in range(N+1)]
bfs(startNode)