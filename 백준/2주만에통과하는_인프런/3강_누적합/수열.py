# 백준#2559 수열(https://www.acmicpc.net/problem/2559)

n, ind = map(int, input().split())

arr = list(map(int, input().split()))


sum = 0
for i in range(ind):
    sum+=arr[i]
maxi = sum

front_idx = 0
for i in range(ind, n):
    sum -= arr[front_idx]
    front_idx+=1
    sum += arr[i]
    maxi = max(maxi, sum)

print(maxi)
