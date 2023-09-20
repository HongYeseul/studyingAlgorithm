# n = int(input())
# result = set()

# result.add(1)
# for i in range(2, int(n**0.5)+1):
#     if(n%i == 0):
#         result.add(i)
#         result.add(int(n/i))

# print(*result)

# for i in range(int(n**0.5)+1, 0, -1):
#     if(n%i == 0):
#         if(i == 1):
#             print(1)
#             print(int(n/i))
#             break
#         else:
#             print(2)
#             print(i, int(n/i))        
#             break
n = int(input())
arr = list(map(int, input().split()))
cnt=0

for j in arr:
    temp = 0
    for i in range(1, int(j**0.5)+1):
        if(j%i == 0 and j!=1):
            temp+=1
    if(temp == 1): cnt+=1

print(cnt)
# print(*result)
