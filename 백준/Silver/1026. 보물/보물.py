import sys

N = int(sys.stdin.readline())
arrA = list(map(int, sys.stdin.readline().split()))
arrB = list(map(int, sys.stdin.readline().split()))

arrA.sort()
arrB.sort()
# arrB.reverse()

result = 0
for i in range(N):
    result += (arrA[i] * arrB[N-1-i])

print(result)