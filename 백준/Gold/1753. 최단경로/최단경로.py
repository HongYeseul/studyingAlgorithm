import sys
from collections import deque
import heapq

V, E = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline())

links = [[] for _ in range(V+1)]
INF = 1e9 # 1,000,000,000
dist = [INF for _ in range(V+1)]

for _ in range(E):
    A,B,C = map(int, sys.stdin.readline().split())
    links[A].append([B, C])

# BFS !

q = []
heapq.heappush(q, [0, start])
dist[start] = 0

while q: # 배열에 아무것도 없으면 false가 된다
    # 우선 순위 큐를 이용해서, 거리를 보고 정렬(dist를 보고 순서를 바꾸는 코드!)
    _w, node = heapq.heappop(q)

    for nxt, weight in links[node]:
        # 1. 각각이 노드에 값을 업데이트
        # 2. 만약에 여러 경로가 있다면 min 비교
        # 3. 시작점으로부터 거리를 확인 후 짧은 순서대로 탐색
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(q, [dist[nxt], nxt])

for j in range(1,V+1):
    if dist[j] == INF:
        print("INF")
    else:
        print(dist[j])
