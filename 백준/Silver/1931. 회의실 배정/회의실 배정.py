# 그리디 문제 중 가장 기본인 회의실 배정 문제
# 해당 알고리즘의 핵심은 항상 제일 빨리 끝나는 회의를 선택하는 것이다.

import sys
N = int(sys.stdin.readline())
time = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(time)

# 입력받은 회의의 끝나는 시간, 시작 시간 순으로 정렬
# 시작 시간 순으로 한 번 더 정리하는 이유
# 3,[[1,3][5,5][4,5]] 순으로 들어왔을 때(종료시간과 시작시간이 같을 경우)
# 반드시 시작시간이 더 빠른 회의를 먼저 선택하는 것이 이득이기 때문이다.
time.sort(key=lambda x:(x[1], x[0]))
# print(time)

lastEndTime = time[0][1]
cnt = 1
for i in range(1, N):
    startTime = time[i][0]
    endTime = time[i][1]

    if lastEndTime <= startTime:
        # print("startTime, endTime", startTime, endTime)
        cnt += 1
        lastEndTime = endTime

print(cnt)
