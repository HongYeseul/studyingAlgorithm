import sys

# 10    20  10  30  20  50
# 1     2   1   3   2   4
# 이전 값들 중 가장 높은 값 +1

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [ 1 for _ in range(N)]

for i in range(N):
    temp = 0
    for j in range(i):
        if arr[j] < arr[i]:
            temp = max(temp, dp[j])
    dp[i] = temp +1

# print(arr)
print(max(dp))