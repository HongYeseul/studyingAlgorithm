# 백준#14232 보석도둑(https://www.acmicpc.net/problem/14232)
# 11653(소인수분해, https://www.acmicpc.net/problem/11653) 문제와 동일한 문제!

n = int(input())

index = 2
temp = n
result = list()
while( index <= (temp**(0.5) +1)):
    while(n % index == 0):
        result.append(index)
        n //= index
    index+=1

if(n!=1): result.append(n)
print(len(result))
print(*result)
