import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(3)] for _ in range(2)]

for k in range(3):
    dp[0][k] = graph[0][k]

# print("start",dp)

for idx in range(1, N):
    for RGB in range(3):

        if RGB == 0: #RED
            dp[1][RGB] = min(dp[0][1], dp[0][2]) + graph[idx][RGB]
        if RGB == 1: #GREEN
            dp[1][RGB] = min(dp[0][0], dp[0][2]) + graph[idx][RGB]
        if RGB == 2: #BLUE
            dp[1][RGB] = min(dp[0][0], dp[0][1]) + graph[idx][RGB]
        
        # print(dp)
    
    for f in range(3):
        dp[0][f] = dp[1][f]
    # print(">> ", dp)

print(min(dp[-1]))