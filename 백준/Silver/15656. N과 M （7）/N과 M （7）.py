N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []

def recurse(n):
    if n == M:
        print(*result)
        return
    
    for i in range(0, N):
        # if arr[i] in result:
        #     continue
        # if len(result) > 0 and max(result) > arr[i]:
        #     continue

        result.append(arr[i])
        recurse(n+1)
        result.pop()

recurse(0)