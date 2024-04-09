def recurs(number):

    if number == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if( len(arr) >= 1 and arr[len(arr)-1] > i):
            continue
        arr.append(i)
        recurs(number+1)
        arr.pop()



N, M = map(int, input().split())
arr = []

recurs(0)
