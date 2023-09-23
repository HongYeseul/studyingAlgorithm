# 백준#14252 공약수열 Platinum4 (https://www.acmicpc.net/problem/14252)

n = int(input())
arr = list(map(int, input().split()))


def _gcd(a, b):
    while(a%b != 0):
        temp = a%b
        a = b
        b = temp
    
    return b

arr.sort()
cnt = 0
for i in range(n-1):
    if( _gcd(arr[i], arr[i+1]) != 1): # 인접한 두 숫자가 서로소가 아니라면
        for j in range(arr[i], arr[i+1]): # arr[i] ~ N ~ arr[i+1] 사이에 서로소가 있는지 판단
            tempA = _gcd(arr[i], j)
            tempB = _gcd(j, arr[i+1])

            if(tempA == 1 and tempB==1): # 서로소가 있다면 숫자 1개만 추가하면 ok
                cnt+=1
                break
            elif(j == arr[i+1]-1): # 서로소가 없다면 숫자 2개를 넣어줘야 함
                cnt+=2

print(cnt)