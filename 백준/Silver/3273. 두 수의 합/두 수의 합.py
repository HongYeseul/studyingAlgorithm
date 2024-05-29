import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

data.sort()
start = 0
end = N -1
cnt = 0

# 투포인터: 가능성을 지워주자.(가능성 없는 것 삭제)
while start < end: # start == end 까지만 실행
    if data[start] + data[end] == target:
        cnt += 1
    
    if data[start] + data[end] >= target:
        end -= 1
    else:
        start += 1

print(cnt)