# 백준 15650 N과M(2) (https://www.acmicpc.net/problem/15650)

def recurse(num):

    if num == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if i in arr:
            continue
        if len(arr) >= 1 and max(arr) > i:
            continue
        arr.append(i)
        recurse(num+1)
        arr.pop()



N, M = map(int, input().split())
arr = []

recurse(0)