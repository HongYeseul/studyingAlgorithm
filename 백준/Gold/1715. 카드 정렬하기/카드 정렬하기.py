import sys, heapq

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    heapq.heappush(heap, num)

total = 0
while len(heap) > 1:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    sumOfNum = num1 + num2
    heapq.heappush(heap, sumOfNum)
    total += (sumOfNum)

print(total)