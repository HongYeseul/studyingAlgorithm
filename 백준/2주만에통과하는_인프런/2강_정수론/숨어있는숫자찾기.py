# 백준#1407 2로 몇번 나눠질까(https://www.acmicpc.net/problem/1407)
#2의 제곱수로 구하는 문제

A, B= map(int, input().split())

# 176 177
# 175! 177! 구해서 차이 계산

A-=1
temp_A = A # 1로 나눴을 때 값
for i in range(1, 99):
    temp_A += ((A//(2**i))*((2**i)-(2**(i-1))))

# print(temp_A)

temp_B = B
for i in range(1, 99):
    temp_B += ((B//(2**i))*((2**i)-(2**(i-1))))

# print(temp_B)

print(temp_B - temp_A)