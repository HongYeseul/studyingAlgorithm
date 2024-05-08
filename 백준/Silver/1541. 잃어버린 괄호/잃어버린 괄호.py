import sys

func = sys.stdin.readline().split('-')
data = []

for arr in func:
    data.append(list(map(int, arr.split('+'))))

# print("data", data)
result = sum(data[0])

for i in range(1, len(data)):
    result -= (sum(data[i]))


print(result)