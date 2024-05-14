import sys

N = int(sys.stdin.readline())

# 날짜 형식을 위해 100 곱해줌
flowers = []
for _ in range(N):
    sm, sd, em, ed = map(int, sys.stdin.readline().split())
    flowers.append([sm*100 + sd, em*100 + ed])
flowers.sort()

# 마지막 꽃의 지는 날
lastEndDate = 301

# 제일 늦게 지는 꽃
tempEndDate = 0

# 선택한 꽃의 개수
cnt = 0

# 모든 꽃이 없어질 때까지 반봅
while flowers:
    # 마지막 꽃의 지는 날이 12월 1일보다 크거나 같을 때와
    # 마지막 꽃의 지는 날이 제일 빨리 피는 꽃보다 작으면 멈춘다.
    if lastEndDate >= 1201 or flowers[0][0] > lastEndDate:
        break

    # 꽃 개수의 길이만큼 반복하여 구간별로 꽃 비교
    for j in range(len(flowers)):
        currentStartDate = flowers[0][0]
        currentEndDate = flowers[0][1]

        # 마지막 꽃의 지는 날이 제일 빨리 피는 꽃보다 크거나 같으면 그 꽃의 지는 날을 확인한다.
        if lastEndDate >= currentStartDate:
            # 그 꽃의 지는 날과 마지막으로 꽃의 지는 날을 비교
            # 그 꽃의 지는 날이 더 크면 더 오래 꽃을 볼 수 있기 때문에
            # 그 꽃의 지는 날을 마지막 꽃의 지는 날로 바꾼다.
            if tempEndDate <= currentEndDate:
                tempEndDate = currentEndDate
            # 꽃 확인시 제거
            flowers.remove(flowers[0])
        
        else: # 꽃의 지는 날이 제일 빨리 피는 꽃보다 작으면 멈춘다.
            break
    
    # 꽃을 선택 했으므로 기록
    lastEndDate = tempEndDate
    cnt += 1

if lastEndDate < 1201:
    print(0)
else:
    print(cnt)
