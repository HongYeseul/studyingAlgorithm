# 백준 15656 N과M(6) (https://www.acmicpc.net/problem/15656)

def recurse():

    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(N):
        arr.append(data[i])
        recurse()
        arr.pop()



N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
arr = []

recurse()