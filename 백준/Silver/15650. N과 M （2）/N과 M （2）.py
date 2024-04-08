N, M = map(int, input().split())

arr = []

def recurse(n):
    if n == M:
        print(*arr)
        return
    
    for i in range(1, N + 1):
        if i in arr :
            continue
        if len(arr) > 0 and arr[len(arr)-1] >= i:
            continue
        arr.append(i)
        recurse(n + 1)
        arr.pop()

recurse(0)