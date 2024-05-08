import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N)]

arr.sort()

dp[0] = arr[0]
for i in range(1, N):
    dp[i] = dp[i-1] + arr[i]

print(sum(dp))