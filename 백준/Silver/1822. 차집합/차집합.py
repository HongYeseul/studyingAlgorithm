import sys

An, Bn = map(int, sys.stdin.readline().split())
arrA = list(map(int, sys.stdin.readline().split()))
arrB = list(map(int, sys.stdin.readline().split()))

# 출력: A - B 개수
# 출력: A - B Arr

dict_b = {}
for i in range(Bn):
    dict_b[arrB[i]] = i

# set_b = set()
# for i in range(Bn):
#     set_b.add(arrB[i])
# print(set_b)

result = []
for target in arrA:
    if target not in dict_b:
        result.append(target)

result.sort()
print(len(result))
if not len(result) == 0:
    print(*result)