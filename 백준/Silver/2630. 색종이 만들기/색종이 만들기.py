from sys import stdin

N = int(input())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
result = [0, 0]

def check(x, y, size):
    num = arr[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if (num != arr[i][j]):
                return False
    return True

def recurse(x, y, size):
    if(check(x, y, size)):
        result[arr[x][y]]+=1
    else:
        nextSize = size//2
        for i in range(2):
            for j in range(2):
                recurse(x + i*nextSize, y + j*nextSize, nextSize)

recurse(0, 0, N)
print(result[0])
print(result[1])
