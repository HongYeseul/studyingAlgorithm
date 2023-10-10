# 백준 15651 N과M(3) (https://www.acmicpc.net/problem/15651)

def recurse(num):

    if num == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        arr.append(i)
        recurse(num+1)
        arr.pop()



N, M = map(int, input().split())
arr = []

recurse(0)