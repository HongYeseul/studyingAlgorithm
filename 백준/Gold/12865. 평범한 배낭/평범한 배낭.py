# 완전 탐색 방법으로 푸는 것!
# (해당 문제는 시간 제한 때문에 DP로 풀어야 함.)
import sys
N, bag = map(int,sys.stdin.readline().split())
items = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 무게 최대 크기만큼 N+1개 만들어줌
dp = [[-1 for _ in range(100_001)] for _ in range(N+1)]

def recur(idx, weight):

    if weight > bag:
        return -9999999
    
    if idx == N:
        return 0

    if dp[idx][weight] != -1:
        return dp[idx][weight]

    # 물건을 넣은 경우와 안 넣은 경우의 max 값을 dp에 저장
    dp[idx][weight] = max(recur(idx +1, weight + items[idx][0]) + items[idx][1], recur(idx +1, weight))

    # # 물건을 넣는 경우
    # recur(idx +1, weight + items[idx][0]) +  items[idx][1]
    # # 물건을 안 넣은 경우
    # recur(idx +1, weight)

    return dp[idx][weight]

recur(0,0)
print(dp[0][0])