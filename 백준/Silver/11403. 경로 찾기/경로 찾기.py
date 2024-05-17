import sys

N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
# print(graph)

INF = float('inf')
visited = [[INF] * (N) for _ in range(N)]

def makeGraph():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                visited[i][j] = 1

def solve():
    for k in range(N): # via
        for i in range(N): # src
            for j in range(N): # dst
                visited[i][j] = min(visited[i][j], visited[i][k]+visited[k][j])

makeGraph()
solve()
# print(visited)

for i in range(N):
    for j in range(N):
        if visited[i][j] == INF:
            print("0", end=" ")
        else: print("1", end=" ")
    print()