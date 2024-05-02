import sys

N = int(sys.stdin.readline())
stairs = [0] * 301
for i in range(1, N + 1):
    stairs[i] = int(sys.stdin.readline())

dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# def solve(idx): # 마지막 계단에서부터 내려가면서 점수 계산
#     if idx == 3: 
#         return stairs[idx]
#     if idx < 3:
#         return -999999
#     # 한 계단 오르기, 두 계단 오르기
#     dp[idx] = max(dp[idx-3] + solve(idx-1) + stairs[idx], dp[idx-2] + solve(idx))
    # return stairs[idx]

for idx in range(4, N+1):
    dp[idx] = max(dp[idx-3] + stairs[idx-1] + stairs[idx], dp[idx-2] + stairs[idx])

# solve(N)
print(dp[N])
