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
