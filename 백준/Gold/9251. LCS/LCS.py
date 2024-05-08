import sys

arrA = list(sys.stdin.readline())
arrB = list(sys.stdin.readline())
sizeA = len(arrA)-1
sizeB = len(arrB)-1
# print(arrA, arrB, sizeA, sizeB)

dp = [[0 for _ in range(sizeA +1)] for _ in range(sizeB+1)]
# print(dp)

for i in range(1, sizeB+1):
    for j in range(1, sizeA+1):
        # 만약에 같은 문자라면: 문자 두개를 제외한 이전 값 +1 저장
        if arrA[j-1] == arrB[i-1]:
            dp[i][j] = dp[i-1][j-1] +1
        # 아니라면: 두 문자 모두 없었을 때와 동일 한 값일 것이므로
        # 없었을 경우(위/아래)중 max 값을 들고 옴 
        else: 
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[sizeB][sizeA])