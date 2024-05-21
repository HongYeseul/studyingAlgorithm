import sys

N = int(sys.stdin.readline())
data = [ int(sys.stdin.readline()) for _ in range(N)]
data.sort()

# x + y + z = k
# x + y = k - z 이용
sum_arr = set()
for i in range(N):
    for j in range(N):
        sum_arr.add(data[i] + data[j])

# print(sum_arr)

def solve():
    for i in range(N -1, -1, -1):
        for j in range(i +1):
            if data[i] - data[j] in sum_arr :
                # print(">>", data[i], data[j])
                return data[i]
    return -1

print(solve())