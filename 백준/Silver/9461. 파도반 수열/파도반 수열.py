import sys

N = int(sys.stdin.readline())

data = [int(sys.stdin.readline()) for _ in range(N)]

dp = [ 0 for _ in range(101) ]
for i in range(1, 101):
    if 1 <= i and i <= 3:
        dp[i] = 1
    else: dp[i] = dp[i - 2] + dp[i - 3]

for x in data:
    print(dp[x])