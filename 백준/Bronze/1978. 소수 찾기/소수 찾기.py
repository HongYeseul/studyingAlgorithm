N = int(input())
arr = list(map(int, input().split()))
result = 0

for x in arr:
    flag = True
    if x == 1:
        flag = False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            flag = False
    if flag == True:
        result+=1

print(result)
