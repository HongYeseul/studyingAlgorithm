import sys
# 이분 탐색을 사용하는 이유
# 1 2 3 4 5 6 7 8 숫자 중에 5를 검색할 때
# 순차 탐색이 아니라 4 > 6 > 5 순으로 탐색의 범위를 반으로 줄이려고 사용한다.

K, N = map(int, sys.stdin.readline().split())

lan = [int(sys.stdin.readline()) for _ in range(K)]

def solve():
    start, end = 1, max(lan)

    while start <= end:
        mid = (start + end) // 2
        lines = 0

        for x in lan:
            lines += (x // mid)
        
        if lines < N:
            end = mid -1
        else:
            start = mid +1
    return end


print(solve())