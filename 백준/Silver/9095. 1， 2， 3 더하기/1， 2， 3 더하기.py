import sys

N = int(sys.stdin.readline())

data = [int(sys.stdin.readline()) for _ in range(N)]
dp = [ 0 for _ in range (N+1)]

result = 0

def solve(num):
    global result

    if num == 0:
        result += 1

    if num >= 3:
        solve(num - 3)
    
    if num >= 2:
        solve(num - 2)
    
    if num >= 1:
        solve(num - 1)
    

for i in range(N):
    solve(data[i])
    print(result)
    result = 0