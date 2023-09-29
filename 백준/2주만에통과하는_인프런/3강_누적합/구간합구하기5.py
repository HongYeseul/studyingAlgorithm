# 백준#11660 구간 합 구하기5 (https://www.acmicpc.net/problem/11660)
from sys import stdin

N, M = map(int, stdin.readline().split())

graph = [list(map(int, stdin.readline().split())) for _ in range(N)]

prefix = [[0 for _ in range(N+1)] for _ in range(N+1)]

for x in range(N):
    for y in range(N):
        prefix[x+1][y+1] = prefix[x][y+1] + prefix[x+1][y] - prefix[x][y] + graph[x][y]

for _ in range(M): 
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1])