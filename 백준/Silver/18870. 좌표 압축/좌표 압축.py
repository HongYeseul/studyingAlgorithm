import sys

N = int(sys.stdin.readline())
sortData = list(map(int, sys.stdin.readline().split()))
arr = sortData.copy()

# set으로 중복 제거후 sorted -> 정렬된 리스트로 만들어짐
sortData = sorted(set(sortData))
# print(sortData)

def search(target):
    start = 0
    end = len(sortData) -1

    while start <= end:
        mid = (start+end) // 2
        if sortData[mid] == target:
            return mid
        elif sortData[mid] < target:
            start = mid +1
        else:
            end = mid -1
    return -1

for target in arr:
    print(search(target), end=" ")