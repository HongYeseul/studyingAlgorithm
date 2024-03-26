from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

def BFS(x, y):
    # 이동할 상, 하, 좌, 우 방향 정의
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 벽이 아니어서 이동 가능한 곳
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] +1   

    # 마지막 값에서 카운트 값 뽑기
    return graph[N-1][M-1]

print(BFS(0,0))