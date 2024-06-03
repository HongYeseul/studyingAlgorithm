import sys
import heapq

# 입력처리
V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

# 그래프 초기화
links = [[] for _ in range(V+1)]
INF = 1e9 # 무한대
dist = [INF for _ in range(V+1)]

# 간선 정보 입력
for _ in range(E):
    A,B,C = map(int, sys.stdin.readline().split())
    links[A].append([B, C])


# 우선순위 큐를 이용한 다익스트라 알고리즘
q = []
heapq.heappush(q, [0, start])
dist[start] = 0

while q: 
    current_distance, node = heapq.heappop(q)

    # 현재 노드까지의 최단거리가 이미 구해진 거리보다 크다면 무시
    if current_distance > dist[node]:
        continue

    for nxt, weight in links[node]:
        # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧을 경우 업데이트
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(q, [dist[nxt], nxt])

# 결과 출력
for j in range(1,V+1):
    if dist[j] == INF:
        print("INF")
    else:
        print(dist[j])
