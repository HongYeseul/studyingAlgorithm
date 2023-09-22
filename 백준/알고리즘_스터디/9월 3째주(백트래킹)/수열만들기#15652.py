# 백준#15652 N과 M(4) Silver3 (https://www.acmicpc.net/problem/15652)
# 9월 3주차 알고리즘 스터디 과제용 문제1
# 인프런 자료구조 강의에서 다룬 부분이 있어 비교적 수월하게 풀 수 있었음

def recurs(number):

    if number == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if( len(arr) >= 1 and arr[len(arr)-1] > i):
            continue
        arr.append(i)
        recurs(number+1)
        arr.pop()



N, M = map(int, input().split())
arr = []

recurs(0)


print("=====================================")
# 다른 분의 코드(참고용!)

def recurs(number):

    if len(arr) == M:
        print(*arr)
        return

    for i in range(number, N+1):
        arr.append(i)
        recurs(i)
        arr.pop()



N, M = map(int, input().split())
arr = []

recurs(1)
