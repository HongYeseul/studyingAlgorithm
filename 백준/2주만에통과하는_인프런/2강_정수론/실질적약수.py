# 백준#2247 실질적 약수(https://www.acmicpc.net/problem/2247)
num = int(input())

# 1!... n!(실질적 약수)를 구해서 다 더하기

arr = list()
sum = 0
for N in range(2, num+1):
    # print("계산 되는 수: ", N)
    for i in range( 2, int(N**0.5) +1):
        if(N%i == 0):
            # arr.append(i)
            # arr.append(N//i)
            # print("더해지는 수: ", i, N//i)
            if(i == N//i): sum+=i
            else: 
                sum+= i
                sum+= (N//i)

print(sum%1_000_000)