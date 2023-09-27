# 백준#2304 창고다각형(https://www.acmicpc.net/problem/2304)

n = int(input())
arr = list()

maxi = 0

for _ in range(n):
    t = list(map(int, input().split()))
    arr.append(t)
    maxi = max(maxi, t[1]) # 막대 기둥 중 제일 높은 값(MAX값) 구하기

arr.sort()

sum = 0
# 첫번째 기둥 ~ 제일 높은 기둥까지 넓이 구하기
xidx = 0
prefix = [0,0]
for i in range(0, n):

    if(prefix[1] >= arr[i][1]): continue

    sum += (arr[i][0] - prefix[0]) * prefix[1]

    xidx = i
    prefix[0] = arr[i][0]
    prefix[1] = arr[i][1]

    if(arr[i][1] == maxi):
        break


# 제일 뒤에있는 기둥 ~ 제일 높은 기둥까지 넓이 구하기
prefix = [0,0]
yidx = 0
for i in range(n-1, xidx-1, -1):

    if(prefix[1] >= arr[i][1]): continue

    sum += (prefix[0]-arr[i][0]) * prefix[1]

    yidx = i
    prefix[0] = arr[i][0]
    prefix[1] = arr[i][1]

    if(arr[i][1] == maxi):
        break


# 제일 높은 기둥이 여러개 일 수 있기 때문에 높은 기둥 면적 구하기
if(xidx != yidx):
    sum+= ((arr[yidx][0]-arr[xidx][0]+1) * maxi)
else: sum+=maxi

print(sum)