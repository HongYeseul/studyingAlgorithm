import sys, heapq
N = int(sys.stdin.readline())

max_heap = []
min_heap = []

for i in range(N):
    num = int(sys.stdin.readline())

    # 두 힙의 크기가 같으면 최대 힙에 숫자를 추가
    # 아니라면 최소 힙에 숫자 추가
    # -> 최대 힙 첫 번째 값이 중간값이 됨
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num) # -num을 넣어서 최대힙을 만들어줌

    else:
        heapq.heappush(min_heap, num)
    
    # 힙 균형 조정
    # 최대 힙의 루트가 최소 힙의 루트보다 크다면, 두 힙의 루트를 교환하여 중간값의 조건을 유지한다.
    if min_heap and -max_heap[0] > min_heap[0]:
        max_top = heapq.heappop(max_heap)
        min_top = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_top)
        heapq.heappush(min_heap, -max_top)
    
    print(-max_heap[0])