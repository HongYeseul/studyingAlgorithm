# 백준#11660 구간 합 구하기5 (https://www.acmicpc.net/problem/11660)

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

for i in range (M):
    x1, y1, x2, y2 = map(int, input().split())

    # prefix = [[0 for _ in range(N+1)] for _ in range(N+1)]

    sum = 0
    for x in range(x1-1, x2):
        for y in range(y1-1, y2):
            sum += graph[x][y]
    print(sum)