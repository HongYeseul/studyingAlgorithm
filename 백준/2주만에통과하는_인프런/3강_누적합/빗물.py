# 백준#14719 빗물(https://www.acmicpc.net/problem/14719)

H, W = map(int, input().split())
arr = list(map(int, input().split()))

maxi = max(arr)

# 처음 기둥 ~ MAX 기둥까지의 물 높이
sum = 0
prefixI = 0
prefixW = 0
tempS = 0
startMaxIdx = 0
for i in range(W):

    if(arr[i] != maxi):
        tempS += arr[i]
    
    if(prefixW >= arr[i]): continue

    sum += (i - prefixI ) * prefixW

    startMaxIdx = i
    prefixI = i
    prefixW = arr[i]

    if(arr[i] == maxi):
        break

sum-=tempS

# MAX 높이 ~ 마지막 기둥까지 물 높이
tempS = 0
prefixI = 0
prefixW = 0
endMaxIdx = 0
for i in range(W-1, startMaxIdx-1, -1):
    if(arr[i] != maxi):
        tempS += arr[i]
    
    if(prefixW >= arr[i]): continue

    sum += (prefixI - i) * prefixW

    endMaxIdx = i
    prefixI = i
    prefixW = arr[i]

    if(arr[i] == maxi):
        break

sum-=tempS

# MAX 높이 ~ MAX 높이까지 물 높이
maxSum = 0
tempS = 0
for i in range(startMaxIdx, endMaxIdx):
    tempS += arr[i]

if(endMaxIdx != startMaxIdx):
    maxSum = (endMaxIdx - startMaxIdx) * maxi
    maxSum -= tempS


print(maxSum + sum)