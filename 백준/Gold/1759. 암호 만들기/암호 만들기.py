L, C = map(int, input().split())
arr = list(input().split())

result = []
arr.sort()

def contains_a():
    for i in ['a', 'i', 'e', 'o', 'u']:
        if i in result:
            return True
    return False

def contains_b():
    cnt = 0
    for i in result:
        if not i in ['a', 'i', 'e', 'o', 'u']:
            cnt += 1
    if cnt >= 2:
        return True
    return False

def recurse():
    if len(result) == L:
        if contains_a() and contains_b() :    
            print(*result, sep="")
            return
    
    for i in arr:
        if len(result) > 0 and result[len(result) - 1] >= i:
            continue
        result.append(i)
        recurse()
        result.pop()

recurse()