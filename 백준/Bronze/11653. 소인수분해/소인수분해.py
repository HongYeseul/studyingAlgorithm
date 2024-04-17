N = int(input())

div = 2
while div <= (int(N**0.5) + 1):
    while N % div == 0:
        print(div)
        N //= div
    div+=1

if (N != 1):
    print(N)