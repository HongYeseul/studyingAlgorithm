import sys

N = int(sys.stdin.readline())

# DP 테이블 초기화
# dp = [0] * (N+1)
dp = {1:0}

def solve(num):
    # print(cnt, num)
    # if num == 1:
    if num in dp.keys():
        # count = min(count, cnt)
        return dp[num]

    # 3으로도 나눠지고 2로도 나눠질 때
    if num % 3 == 0 and num % 2 == 0:
        dp[num] = min(solve(num //3)+1, solve(num // 2) +1)

    # 3으로 나눠질 때
    elif num % 3 == 0:
        dp[num] = min(solve(num//3)+1, solve(num-1)+1)

    # 2로 나눠질 때
    elif num % 2 == 0:
        dp[num] = min(solve(num // 2)+1, solve(num-1)+1)

    # 1을 뼀을 때
    else:
        dp[num] = solve(num -1) +1
    
    return dp[num]

print(solve(N))
# print(dp)