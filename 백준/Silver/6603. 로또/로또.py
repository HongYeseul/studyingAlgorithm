arr = list(map(int, input().split()))
n = arr.pop(0)
arr.sort()
result = []

def recurse():
    if len(result) == 6:
        print(*result)
        return
    
    for i in arr:
        if len(result) > 0 and i <= max(result):
            continue

        result.append(i)
        recurse()
        result.pop()

while (n!= 0):
    recurse()
    arr = list(map(int, input().split()))
    print()
    n = arr.pop(0)
    arr.sort()