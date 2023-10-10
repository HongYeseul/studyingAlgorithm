# 백준 15654 N과M(5) (https://www.acmicpc.net/problem/15654)

def recurse():

    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(N):
        if(data[i] in arr):
            continue
        arr.append(data[i])
        recurse()
        arr.pop()



N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
arr = []

recurse()