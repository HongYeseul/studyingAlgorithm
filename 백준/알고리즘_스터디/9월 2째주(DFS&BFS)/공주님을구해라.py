#17836 공주님을 구해라! Gold5 (https://www.acmicpc.net/problem/17836)
#9월 2주차 알고리즘 스터디 과제용 문제2

from collections import deque

Y, X, T = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(Y) ]

# 명검 '그람' 위치 찾기
swordX, swordY = 0,0
for x in range(X):
    for y in range(Y):
        if(graph[x][y] == '2'):
            swordX = x
            swordY = y
            break

# 명검 '그람'까지의 최소거리 구하기
queue = deque()
queue.append((0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0 for _ in range(X)] for _ in range(Y) ]
visited[0][0] = 1
t = 0
flag=0
maxi = 0

for x in range (X) : #생각해보니까 얘는 항상 0.0에서 시작하니까 for문 안돌려도됨 다시 짜...
    for y in range (Y) :
        if graph[y][x] == '0':
            visited = [[0 for _ in range(X)] for _ in range(Y) ]

        while queue and flag==0:
            x, y = queue.popleft()
            print(x, y)
            visited[x][y] = 1
            print(visited)
            t+=1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= ny < Y and 0 <= nx < X:
                    print("nx, ny: ", nx, ny, graph[nx][ny], " visited: ", visited[x][y]+1) 
                    if graph[nx][ny] == '0': 
                        if visited[nx][ny] == 0:
                            visited[nx][ny] = (visited[x][y])+1
                            maxi = max(maxi, visited[ny][nx])
                            queue.append((nx, ny))

                    if graph[nx][ny] == '1': #벽인 경우 무시
                        continue

                    if graph[nx][ny] == '2': #칼을 찾을 경우 종료
                        flag=1
                        break
        if(flag==1): break
    if(flag==1): break

print(visited)
print(flag, t)


# 명검 '그람'이 있는 위치부터 공주가 있는 곳 까지의(N-1, M-1)까지의 거리 구하기