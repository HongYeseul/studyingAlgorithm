import sys, heapq

# 1. 문제를 데드라인 기준으로 오름차순 정렬
# 2. 현재 시간(문제 푼 개수)이 데드라인보다 작으면 문제를 풀고 컵라면 수를 큐에 추가
# 3. 만약 현재시간(문제 푼 개수)이 데드라인을 초과하면, 큐에 있는 가장 적은 컵라면 수를 가진 문제와 현재 문제를 비교
# 컵라면 수가 더 많은 문제 선택

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
data.sort()

heap = []

for deadline, ramen in data:
    heapq.heappush(heap, ramen)

    # 일단 힙에 넣어두고
    # 데드라인보다 넘어섰다면 최소값 pop
    if len(heap) > deadline:
        heapq.heappop(heap)

print(sum(heap))