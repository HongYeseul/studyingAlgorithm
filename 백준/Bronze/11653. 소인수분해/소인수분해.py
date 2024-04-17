n = int(input())
result = list()

for i in range(2, int(n**0.5)+1):
    if(n%i == 0):
        result.append(i)
        result.append(int(n/i))

if(n == 1):
    exit()

if(len(result) == 0):
    print(n)
    exit()

for i in result:
    flag = 1
    prime = i
    for j in range(2, int(i**0.5)+1): # 소수인지 알아내는 함수
        if(i%j == 0):
            prime = 0
            flag = -1

    if(flag == 1):
        while(n%prime == 0):
            n = int(n/prime)
            print(prime)