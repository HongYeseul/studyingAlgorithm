# 핵심
# 교차된 줄이 없는 그룹이 최대 였을 때 = 오름차순인 그룹의 최대

import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [1 for _ in range(N)]
arr.sort()


for i in range(N):
    temp = 0
    for j in range(i):
        beforeN = arr[i][1]
        currentN = arr[j][1]
        if currentN < beforeN:
            # print("beforeN, currentN", beforeN, currentN)
            temp = max(temp, dp[j])
    dp[i] = temp+1

# N - LIS(전체 전깃줄 - 교차 없는 전깃줄 중 최대 길이)
print(N - max(dp))
