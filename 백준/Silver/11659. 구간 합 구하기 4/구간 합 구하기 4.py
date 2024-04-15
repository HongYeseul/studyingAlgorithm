import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum = []
result = 0
for i in arr:
    result+=i
    sum.append(result)

for i in range(M):
    start, end = map(int, input().split())
    if start == 1:
        print(sum[end-1])
    else:
        print(sum[end-1] - sum[start-2])