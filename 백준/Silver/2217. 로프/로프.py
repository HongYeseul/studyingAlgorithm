import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

arr.sort()
result = []

for x in arr:
    result.append(x * N)
    N -= 1


print(max(result))