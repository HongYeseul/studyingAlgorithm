# 백준#3020 개똥벌레(https://www.acmicpc.net/problem/3020)
from sys import stdin

N, H = map(int, stdin.readline().split())
arr = list()

for i in range(N):
    arr.append(int(stdin.readline()))


prefix = [ 0 for _ in range(H+1)]
sum = [0 for _ in range(H+1)]
for i in range(N):
    if(i%2 == 0): # 짝수
        prefix[0] += 1
        prefix[arr[i]] += -1
    else: #홀수
        prefix[H - arr[i]] += 1
    
    # print(prefix)

mini = prefix[0]
for i in range(1, H+1):
    sum[i] += sum[i-1]+prefix[i-1]
    if(sum[i] <= mini):
        mini = sum[i]

cnt = 0
for i in range(1, H+1):
    if(sum[i] == mini):
        cnt+=1

# print(prefix)
# print(sum)
print(mini, cnt)