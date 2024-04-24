import sys
sys.setrecursionlimit(99999999)

N = int(sys.stdin.readline())
interview = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [-1 for _ in range(N+1)]
answer = 0

def recurse(idx):
    global answer

    if idx > N:
        return -999999999
    
    if idx == N :
        return 0
    
    # 만약 값이 있으면 이미 찾았다는 뜻이므로 pass
    if dp[idx] != -1:
        return dp[idx]

    # 상담을 받거나, 안 받거나 그 중에서 더 많은 '돈'을 버는 경우 내 DP 테이블에 저장하겠다.
    dp[idx] = max(recurse(idx + interview[idx][0]) + interview[idx][1], recurse(idx+1))

    return dp[idx]

recurse(0)

print(dp[0])