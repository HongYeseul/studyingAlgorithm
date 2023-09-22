# 백준#2247 실질적 약수(https://www.acmicpc.net/problem/2247)
# 1!... n!(실질적 약수)를 구해서 다 더하기

#### ⭐ python으로 하면 시간초과, pypy로 하면 통과
A = int(input())

temp_A = 0

for i in range(2, int(A/2+1)):
    temp_A+= i*(A//i -1) % 1000000

print(temp_A % 1000000)

## 이 분 글 참고(https://cobokjang.tistory.com/14)해서 나중에 다시 풀어볼 것