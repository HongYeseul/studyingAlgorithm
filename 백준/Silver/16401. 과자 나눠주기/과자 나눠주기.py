import sys

cousinN, snackN = map(int, sys.stdin.readline().split())
snack = list(map(int, sys.stdin.readline().split()))

# sorting이 되어있으나 없으나 값에 영향을 미치지 않으므로 sort 하면 시간 초과남
start, end = 1, max(snack)
result = 0
while start <= end:
    mid = (start + end) // 2

    n = 0
    for snack_length in snack:
        n += (snack_length // mid)
    
    if n >= cousinN:
        start = mid +1
        result = mid
    else:
        end = mid -1

print(result)