import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum = [0]
result = 0
for i in arr:
    result+=i
    sum.append(result)

for i in range(M):
    start, end = map(int, input().split())
    print(sum[end] - sum[start-1])
