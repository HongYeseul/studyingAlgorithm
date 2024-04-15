import sys

N, M, B = map(int, sys.stdin.readline().split())
ground = []
for _ in range(N):
    ground.extend(map(int, sys.stdin.readline().split()))

time = [0 for i in range(257)] # time[k]에 땅높이가 k일때의 소요시간 저장
height = 0

for g in range(257):
    block = B # 각 땅 높이마다 남은 block 수 기록

    for i in ground: # 모든 집터 순회
        if i <= g: # 높은 땅 만들어야 할 때, 땅을 채워준다
            block -= g - i
            time[g] += g - i
        else: # 낮은 땅 만들어야 할 때, 땅을 캐온다
            block += i - g
            time[g] += 2 * (i - g)
    
    if block >= 0 and time[g] <= time[height]:
        height = g

print(time[height], height)