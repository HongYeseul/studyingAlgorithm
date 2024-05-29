import sys

N, target = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, sys.stdin.readline().split())))

start = 0
end = N-1
cnt = 0
temp = 0

while start <= end: # start와 end가 동일할 때까지 판단해야함.
    if data[end] == target:
        cnt += 1
        end -= 1
        continue

    if start == end:
        # start, end 동일하면 자투리로 남는 것이 있다는 뜻
        temp += 1
        break
    
    if data[start] + data[end] >= target/2:
        cnt += 1
        start += 1
        end -= 1
    else: # 두개를 더했는데 target/2보다 작으면 자투리로 남겨둠
        temp += 1
        start += 1

# 병 두개를 가져다주면 하나에 반을 채워주므로
# 병 두개는 무조건 Target/2, +1개가 있으면 또 target/2를 주므로
# 자투리 // 3을 더해준다
print(cnt + (temp//3))