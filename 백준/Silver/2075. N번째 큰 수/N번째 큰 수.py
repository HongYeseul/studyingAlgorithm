import sys, heapq

# 최댓값 5개가 들어가야 한다
# heap의 크기가 5개로 유지되도록 한다
#  -> 현재 heap 내 최소값보다 작은 값이 들어온다면 무시한다

N = int(sys.stdin.readline())
heap = []

arr = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))

    for num in a:
        if len(heap) < N:
            heapq.heappush(heap, num)
        
        if heap[0] < num:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

print(heap[0])
