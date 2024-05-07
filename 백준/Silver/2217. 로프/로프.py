# 핵심
# 로프들의 최소 값 * n개 만큼만 최대로 들 수 있다.
# 예
# [1, 8, 9] 로프의 최대 무게 = 3
# [8, 9] 로프의 최대 무게 = 16
# [9] 로프의 최대 무게 = 9

import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

arr.sort()
result = []

for x in arr:
    result.append(x * N)
    N -= 1


print(max(result))
