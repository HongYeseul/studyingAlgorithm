N = int(input())
arr = []

max_height = 0
for _ in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
    max_height = max(max_height, data[1])

arr.sort()

# print("max idx:", maxi)

result = 0
start_idx = 0
prefix = [0,0]
for i in range(0,N):
    if prefix[1] >= arr[i][1]: continue
    result += (arr[i][0] - prefix[0]) * prefix[1]

    start_idx = i
    prefix = arr[i]

    if arr[i][1] == max_height:
        break

prefix = [0,0]
end_idx = 0
for i in range(N-1, start_idx - 1, -1):
    if prefix[1] >= arr[i][1]: continue
    result += (prefix[0] - arr[i][0]) * prefix[1]

    end_idx = i
    prefix = arr[i]

    if arr[i][1] == max_height:
        break

# if start_idx != end_idx:
result += ((arr[end_idx][0] - arr[start_idx][0] +1) * max_height)
# else:
    # result += max_height

print(result)