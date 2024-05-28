import sys, heapq

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(arr) == 0:
            print(0)
            continue
        print(heapq.heappop(arr)[1])
        continue

    heapq.heappush(arr, [num*-1, num])