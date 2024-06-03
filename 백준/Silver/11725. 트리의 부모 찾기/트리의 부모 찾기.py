import sys
sys.setrecursionlimit(999999)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

parent = [0 for _ in range(N+1)]

def recurse(node, prev):
    parent[node] = prev

    for next_node in graph[node]:
        if next_node == prev:
            continue
        recurse(next_node, node)


recurse(1, 0)

for n in parent[2:]:
    print(n)