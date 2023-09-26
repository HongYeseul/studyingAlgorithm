# 백준#1912 수열(https://www.acmicpc.net/problem/1912)

n = int(input())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(n+1)]

for i in range (n):
    prefix[i+1] = prefix[i]+arr[i]

answer = []
maxi = arr[0]
for i in range(n):
    prefix[i+1] = max(prefix[i]+arr[i], arr[i])
    maxi = max(prefix[i+1], maxi)


print(prefix)
print(maxi)