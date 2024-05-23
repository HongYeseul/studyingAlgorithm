import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(tree)
while start <= end:
    mid = (start + end) // 2
    
    get = 0
    for l in tree:
        if l > mid:
            get += (l - mid)

    if get == M:
        # print(">>", get, start, end, mid)
        end = mid
        break
    if get < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)