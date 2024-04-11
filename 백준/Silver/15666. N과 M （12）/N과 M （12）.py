N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []
# visitied = [0] * N

def recurse():
    check = 0
    if len(result) == M:
        print(*result)
        return
    
    for i in range(N):
        if len(result) > 0 and arr[i] < max(result):
            continue

        if check != arr[i]:
            result.append(arr[i])
            # visitied[i] = 1
            check = arr[i]
            recurse()
            result.pop()
            # visitied[i] = 0

recurse()