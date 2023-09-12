#2589 보물섬 (https://www.acmicpc.net/problem/2589)

from collections import deque

Y, X = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(Y) ]

maximum = 0

for y in range(Y) :
    for x in range(X):
        if graph[y][x] == 'L':
            visited = [[0 for _ in range(X)] for _ in range(Y) ]
            distance = [[0 for _ in range(X)] for _ in range(Y) ]

            #BFS
            q = deque()
            q.append([y, x])
            visited[y][x] = 1

            while q :
                ey, ex = q.popleft()
                #4방향 탐색(2차원 DP)
                for dy, dx in [[0,1], [1,0], [-1, 0], [0, -1]]:
                    ny, nx = ey+dy, ex+dx
                    if 0 <= ny < Y and 0 <= nx < X:
                        if graph[ny][nx] == 'L':
                            if visited[ny][nx] == 0: # 방문한 적 없을 때
                                visited[ny][nx] = 1
                                distance[ny][nx] = distance[ey][ex]+1
                                maximum = max(maximum, distance[ny][nx])
                                q.append([ny, nx] )

print(maximum)