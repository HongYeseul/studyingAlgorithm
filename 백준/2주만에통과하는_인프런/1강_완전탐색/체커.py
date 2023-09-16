#1090 체커 Platinum4 (https://www.acmicpc.net/problem/1090)

n = int(input())
x = []
y = []

for i in range(n):
    tx, ty = map(int, input().split())
    x.append(tx)
    y.append(ty)

print(x, y)

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

