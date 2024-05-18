import sys

N = int(sys.stdin.readline())
INF = float('inf')
graph = [[INF] * (N+1) for _ in range(N+1)]

while (True):
    a, b = map(int, sys.stdin.readline().split())
    if a == -1: break
    graph[a][b] = 1
    graph[b][a] = 1

# for i in range(N+1):
#     print(*graph[i])

def floyd():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    graph[i][j] = 1
                    continue
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

floyd()

vector = [ 0 for _ in range(N+1)]
for i in range(1, N+1):
    graph[i].remove(INF)
    vector[i] = max(graph[i])

# for i in range(N+1):
#     print(*graph[i])
# print(vector)

vector.remove(0)
m = min(vector)
result = []
for i in range(N):
    if m == vector[i]:
        result.append(i +1)

print(m, len(result))
print(*result)