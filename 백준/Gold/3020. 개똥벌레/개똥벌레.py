import sys

N, H = map(int, sys.stdin.readline().split())
cave = [0]
for _ in range(N):
    cave.append(int(sys.stdin.readline()))

# print("cave:", cave)
prefix = [0] * (H+1)

for i in range(1, N+1):
    if i % 2 == 1:
        prefix[1] += 1
        prefix[cave[i]+1] -= 1
    
    if i % 2 == 0:
        # prefix[H + 1] -= 1
        prefix[H +1  -cave[i]] += 1

# print(prefix)

for i in range(1, H+1):
    prefix[i] = prefix[i-1] + prefix[i]

# print(prefix)

min_cnt = prefix[1]
for i in range(1, H):
    if min_cnt > prefix[i]:
        min_cnt = prefix[i]

cnt = 0
for i in range(1, H+1):
    if prefix[i] == min_cnt:
        cnt+=1

print(min_cnt, cnt)