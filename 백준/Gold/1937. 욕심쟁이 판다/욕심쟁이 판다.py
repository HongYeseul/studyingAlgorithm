import sys
sys.setrecursionlimit(99999999)

N = int(input())
data = [list(map(int, input().split())) for _ in range(N) ]
dp = [[0 for _ in range (N)] for _ in range(N)]

def solve(x, y):
    if dp[x][y] != 0:
        return dp[x][y]

    for [i, j] in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ex = x + i
        ey = y + j
        if 0 <= ex < N and 0 <= ey < N:
            if data[x][y] < data[ex][ey]:
                dp[x][y] = max(dp[x][y], solve(ex, ey)+1)
    
    return dp[x][y]


# 1. 모든 점을 방문한다.
# 2. 방문한 뒤에 이동할 수 있는 모든 경우의 수를 재귀로 구현한다.
# 3. 재귀로 구현한 뒤 DP로 바꾼다!

# 아래는 재귀로 구현한 코드
def recurse(x, y):

    point = 0
    for [i, j] in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
        ex = x + i
        ey = y + j
        if 0 <= ex < N and 0 <= ey < N:
            if data[x][y] < data[ex][ey]:
                point = max(point, recurse(ex, ey) + 1)
    
    return point
    # return max(recurse(x-1, x), recurse(x+1, y), recurse(x, y-1), recurse(x, y+1))



for x in range(N):
    for y in range(N):
        solve(x, y)

print(max(map(max, dp))+1)