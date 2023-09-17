#1090 체커 Platinum4 (https://www.acmicpc.net/problem/1090)

# 1번 아이디어
# x, y를 구분 해서 계산 해 준 뒤 합쳐서 최소값을 알려주면 된다!

# 2번 아이디어
# 우리가 한 곳에서 모일 때, 비용을 최소화 하기 위해서는 우리의 집 중 한 곳에서 모이면 된다.

# 3번 아이디어
# 최소 거리를 계산하고 싶다. 그리고, 2명이 모여야 한다.
# 그 점에서, 가까운 두 명의 거리만 더해주면 되지 않을까?

# A번집, B번집, C번집
# [1, 2, 3] // [3, 4, 5] // [2, 2, 5]
# 두 사람이 모일 수 있는 최소 거리는 3!

# 만약 1차원이라면 점들 중 한 곳에 모이면 되는 것이 맞지만,
# 2차원으로 커진다면 x축의 정답가능성 n개와 y축의 정답 가능성 n개를 모두 조합한 경우의 수인 n*n개를 확인하여 정답을 찾아야 한다.
# 따라서 해당 예시(15,14) (15,16) (14,15) (16,15)의 경우
# (14, 14) (14, 15) (14, 16) (15,14) (15,15) (15,16) ... (16,16) 총 9개의 좌표를 확인 해야 한다! -> 아님!! (아래 덧붙임 참고)
# -덧붙임-
# 해당 좌표를 확인 한다는 것은 총 3*3의 9번을 확인한다는 것이 아니다. [x]*[y]의 값을 돌면서 n*n번을 확인하게 된다.
# 그러므로 좌표가 16*16의 좌표에 4개의 점이 있다면 16*16개의 좌표를 모두 확인하는 것이 아닌, n*n인 16개의 좌표만 확인하게 된다.
# 내가 간과 했던 것은 2번 아이디어(비용을 최소화 하기 위해서는 우리의 집 중 한 곳에 모이면 된다.)와 마지막 단락 2번째 줄이었던 것 같다. 좌표 값에 해당하지 않는 숫자들은 찾아 볼 필요가 없었다.
# 해당 내용을 이해한 바탕으로 블로그에 간략한 그림을 그려 기록했다.
# 참고! (https://velog.io/@yeseul/230917-%EB%B0%B1%EC%A4%801090-%EC%B2%B4%EC%BB%A4)

######################## 기존 코드 ############################

n = int(input())
x = []
y = []

for i in range(n):
    tx, ty = map(int, input().split())
    x.append(tx)
    y.append(ty)

minX = min(x)
minY = min(y)
maxX = max(x)
maxY = max(y)

sum = [ list(0 for _ in range(n)) for _ in range((maxY-minY+1)*(maxX-minX+1)) ]

for co in range(n):
    cnt = 0
    for i in range(minX, maxX+1):
        for j in range(minY, maxY+1):
            # 체커가 있는 위치에서 모든 좌표로의 거리 계산
            sum[cnt][co] = abs(i-x[co])+abs(j-y[co])

            cnt+=1

# k 번째 수가 k개 만큼 모였을 때 이동해야 하는 횟수 구하기
# 해당 개수만큼 더했을 때 최소가 되는 수

for i in range (n-1):
    sum[i].sort()

m = list(100_000_000 for _ in range( n ))
for i in range( n ):
    for j in range( len(sum) ):
        s = 0
        for k in range(i+1):
            s += sum[j][k]
        if(m[i] > s):
            m[i] = s

print(*m)

###############기존 짰던 코드와 유사하게 수정한 방법(3차 - 기존 코드와 제일 유사)################

n = int(input())
x = []
y = []

for i in range(n):
    tx, ty = map(int, input().split())
    x.append(tx)
    y.append(ty)

sum = [ list(0 for _ in range(n)) for _ in range( n*n ) ]

for co in range(n):
    cnt = 0
    for i in x:
        for j in y:
            # 체커가 있는 위치에서 모든 좌표로의 거리 계산
            sum[cnt][co] = abs(i-x[co])+abs(j-y[co])

            cnt+=1

# k 번째 수가 k개 만큼 모였을 때 이동해야 하는 횟수 구하기
# 해당 개수만큼 더했을 때 최소가 되는 수

for i in range (n*n):
    sum[i].sort()


m = list(100_000_000 for _ in range( n ))
for i in range( n ):
    for j in range( len(sum) ):
        s = 0
        for k in range(i+1):
            s += sum[j][k]
        if(m[i] > s):
            m[i] = s

print(*m)

############기존 짰던 코드와 유사하게 수정한 방법(2차, 비효율적)##############

n = int(input())
x = []
y = []

for i in range(n):
    tx, ty = map(int, input().split())
    x.append(tx)
    y.append(ty)
    
dist = list()

for i in x:
    for j in y:
        # 체커가 있는 위치에서 다른 좌표로의 거리 계산
        d = []
        for c in range(n):
            d.append(abs(i-x[c])+abs(j-y[c]))

        d.sort()
        dist.append(d)

m = list(100_000_000 for _ in range( n ))
for i in range( n*n ):
    for j in range( n ):
        s = 0
        for k in range(j+1):
            s += dist[i][k]
        if(m[j] > s):
            m[j] = s

print(*m)



###########인강 강사님 코드 구조로 수정한 방법(1차, 효율적)#############

n = int(input())
x = []
y = []
result = [-1]*n


for _ in range(n):
    tx, ty = map(int, input().split())
    x.append(tx)
    y.append(ty)

for i in x:
    for j in y:
        # 체커가 있는 위치에서 다른 좌표로의 거리 계산
        dist = []
        for k in range(n):
            dist.append(abs(x[k]-i)+abs(y[k]-j))
        
        # 가까운 순으로 정렬하기
        dist.sort()

        # m개의 체커가 같은 곳에 모일 때의 최소 비용을 계산
        tmp = 0
        for m in range( len(dist)):
            d = dist[m]
            tmp += d
            if result[m] == -1:
                result[m] = tmp
            else:
                result[m] = min(tmp, result[m])

print(*result)