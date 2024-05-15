import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(N+1)]

for arr in graph:
    arr.sort()

# 메인 아이디어: visited의 값을 누적합으로 하여 dept를 구한다.
def bfs(node):
    queue = deque([node])
    visited[node] = 1

    while(queue):
        friendNum = queue.popleft()

        for nxt in graph[friendNum]:
            if visited[nxt] == 0:
                queue.append(nxt)
                visited[nxt] = visited[friendNum] +1

def solve():
    bfs(1)
    cnt = 0
    # 노드 레벨 3까지의 값을 구함. 나, 내 친구, 내 친구의 친구
    # 나는 포함이 되어야 하지 않으므로 index 2부터 검색
    for i in range(2, N+1):
        if 0 < visited[i] <= 3:
            cnt += 1
    # print(visited)
    print(cnt)

solve()