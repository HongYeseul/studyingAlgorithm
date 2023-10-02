# 백준#3020 개똥벌레(https://www.acmicpc.net/problem/3020)

N, H = map(int, input().split())
arr = list()

for i in range(N):
    arr.append(int(input()))


prefix = [ 0 for _ in range(H+1)]
for i in range(N):
    
    if(i%2 == 0): # 짝수
        prefix[0] += 1
        prefix[arr[i]] += -1
    else: #홀수
        prefix[H - arr[i]] += 1
    
    # print(prefix)

sum = [0 for _ in range(H+1)]
mini = prefix[0]
for i in range(1, H+1):
    sum[i] += sum[i-1]+prefix[i-1]
    # print("비교: ", sum[i], mini)
    if(sum[i] <= mini):
        # print("smallest: ",sum[i])
        mini = sum[i]

cnt = 0
for i in range(1, H+1):
    if(sum[i] == mini):
        cnt+=1

# print(prefix)
# print(sum)
print(mini, cnt)