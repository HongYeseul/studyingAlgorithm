import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
toFind = list(map(int, sys.stdin.readline().split()))

arr.sort()

def search(target):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid +1
        else:
            end = mid -1
    return 0

for target in toFind:
    print(search(target), end=" ")