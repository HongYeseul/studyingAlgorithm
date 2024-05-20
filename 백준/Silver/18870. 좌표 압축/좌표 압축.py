import sys

N = int(sys.stdin.readline())
sortData = list(map(int, sys.stdin.readline().split()))
arr = sortData.copy()

# set으로 중복 제거후 sorted -> 정렬된 리스트로 만들어짐
sortData = sorted(set(sortData))

# 첫 번째 풀이: sort된 리스트 set을 binary search로 찾아 index 반환
# def search(target):
#     start = 0
#     end = len(sortData) -1

#     while start <= end:
#         mid = (start+end) // 2
#         if sortData[mid] == target:
#             return mid
#         elif sortData[mid] < target:
#             start = mid +1
#         else:
#             end = mid -1
#     return -1

# for target in arr:
#     print(search(target), end=" ")

# 수정한 풀이: dictionary에 idx 값을 저장해서 바로 꺼낼 수 있도록 수정
n_dict = {}
for i in range(len(sortData)):
    n_dict[sortData[i]] = i

for target in arr:
    print(n_dict[target], end=" ")