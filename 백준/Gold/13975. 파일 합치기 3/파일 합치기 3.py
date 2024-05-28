import sys, heapq

N = int(sys.stdin.readline())

for _ in range(N):
    n = int(sys.stdin.readline())
    heap = list(map(int, sys.stdin.readline().split()))

    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)
        s = num1 + num2

        total += s
        heapq.heappush(heap, s)
    print(total)

