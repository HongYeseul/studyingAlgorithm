import sys
N = int(sys.stdin.readline())

def makeDistance(a, b):
    cnt = 0
    for i in range(4):
        if (a[i] != b[i]):
            cnt += 1
    return cnt

def solve():
    n = int(sys.stdin.readline())
    arr = list(sys.stdin.readline().split())

    if n > 32:
        return 0
    
    dist = 100_001

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or j == k or i == k:
                    continue
                
                ab = makeDistance(arr[i], arr[j])
                bc = makeDistance(arr[j], arr[k])
                ac = makeDistance(arr[i], arr[k])
                dist = min(ab+bc+ac, dist)
    return dist

for _ in range(N):
    print(solve())