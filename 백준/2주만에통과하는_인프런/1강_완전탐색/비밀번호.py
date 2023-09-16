# 1816 비밀번호 bronze1(https://www.acmicpc.net/problem/1816) 

n = int(input())

for _ in range(n):
    number = int(input())
    flag = 0
    for i in range(2, 1_000_001):
        if(number%i == 0):
            flag = 1
            break
    if(flag == 1): print("NO")
    else: print("YES")