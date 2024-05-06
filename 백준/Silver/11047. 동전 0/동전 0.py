import sys

N, K = map(int, sys.stdin.readline().split())
coins = list(int(sys.stdin.readline()) for _ in range(N))

result = 0

for i in range(N)[::-1]:
    if (K >= coins[i]):
        result += (K // coins[i]) 
        K %= coins[i]
    if K == 0:
        break


print(result)