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
# (14, 14) (14, 15) (14, 16) (15,14) (15,15) (15,16) ... (16,16) 총 9개의 좌표를 확인 해야 한다!

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