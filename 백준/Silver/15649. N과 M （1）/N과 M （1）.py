
def recurse(num):

    if num == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if i in arr:
            continue
        arr.append(i)
        recurse(num+1)
        arr.pop()



N, M = map(int, input().split())
arr = []

recurse(0)