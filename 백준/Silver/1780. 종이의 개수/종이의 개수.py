from sys import stdin

N = int(input())

arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
result = [0, 0, 0]

def check(startX, startY, n):
    num = arr[startX][startY]
    for i in range(startX, n + startX):
        for j in range(startY, n + startY):
            if (num != arr[i][j]) :
                return False
    return True

def func(startX, startY, n):
    # 모든 칸이 같은 수라면
    if (check(startX, startY, n)):
        result[arr[startX][startY] +1]+=1
        return
    else: # 섞여있는 배열이라면 나누기
        size = n // 3
        for i in range(3):
            for j in range(3):
                func(startX + size * i, startY + size * j, size)



func(0, 0, N)
print(result[0], result[1], result[2])


