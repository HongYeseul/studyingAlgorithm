import sys

N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))

result = 0
for i in range(N):
    result += ((N - i) * arr[i])

print(result)