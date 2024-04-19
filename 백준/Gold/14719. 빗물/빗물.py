# 백준#14719 빗물(https://www.acmicpc.net/problem/14719)

H, W = map(int, input().split())
arr = list(map(int, input().split()))

maxi = max(arr)

sum = 0
prefixI = 0
prefixW = 0
tempS = 0
startMaxIdx = 0
for i in range(W):

    # print("tempS +",arr[i])
    if(arr[i] != maxi):
        tempS += arr[i]
    
    if(prefixW >= arr[i]): continue

    # print("prefix i: ",i, prefixI, prefixW)
    sum += (i - prefixI ) * prefixW

    startMaxIdx = i
    prefixI = i
    prefixW = arr[i]

    if(arr[i] == maxi):
        break

sum-=tempS

# print("================START=================")
# print(sum, tempS)
# print("sum, startMaxIdx")
# print(sum,startMaxIdx)
# print("=================================")

tempS = 0
prefixI = 0
prefixW = 0
endMaxIdx = 0
for i in range(W-1, startMaxIdx-1, -1):

    # print("tempS +",arr[i])
    if(arr[i] != maxi):
        tempS += arr[i]
    
    if(prefixW >= arr[i]): continue

    # print("prefix i: ",i, prefixI, prefixW)
    sum += (prefixI - i) * prefixW

    endMaxIdx = i
    prefixI = i
    prefixW = arr[i]

    if(arr[i] == maxi):
        break

# print("TempS: ", tempS)
sum-=tempS

# print("==============MIDDLE===================")
# print(sum, tempS)
# print("sum, endMaxIdx")
# print(sum, endMaxIdx)
# print("=============END====================")
# print(startMaxIdx, endMaxIdx)

maxSum = 0
tempS = 0
for i in range(startMaxIdx, endMaxIdx):
    # if(arr[i] == maxi): continue
    # print("i: ", i)
    tempS += arr[i]

if(endMaxIdx != startMaxIdx):
    maxSum = (endMaxIdx - startMaxIdx) * maxi
    # print("SUM: ", maxSum)
    maxSum -= tempS
# print(maxSum, tempS)

# print("=========RESULT=======")
print(maxSum + sum)