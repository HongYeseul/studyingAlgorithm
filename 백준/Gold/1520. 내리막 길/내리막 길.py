N, M = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(N)]

dp = [[-1 for _ in range(M)] for _ in range(N)]

def solve(x, y):
    if x == (N-1) and y == (M-1):
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    route = 0
    for [i, j] in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ex = x + i
        ey = y + j
        if 0 <= ex < N and 0 <= ey < M:
            if data[x][y] > data[ex][ey]:
                route += solve(ex, ey)
    
    dp[x][y] = route

    return dp[x][y]

# print(dp)
print(solve(0,0))