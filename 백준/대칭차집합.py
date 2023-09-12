#1269 대칭 차집합 (https://www.acmicpc.net/problem/1269)

aNum, bNum = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))


print(len(a - b)+len(b-a))