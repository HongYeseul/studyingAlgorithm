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

print(N - max(dp))