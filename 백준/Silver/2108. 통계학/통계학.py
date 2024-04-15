import sys
from collections import Counter

N = int(sys.stdin.readline())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline()))

data.sort()

# 산술평균
print(round(sum(data)/ N)) 

# 중앙값
print(data[N//2]) 

# 최빈값
numCountList = Counter(data).most_common()
if len(numCountList) > 1 and numCountList[0][1] == numCountList[1][1]:
    print(numCountList[1][0])
else:
    print(numCountList[0][0])

# 범위
print(data[N-1] - data[0])