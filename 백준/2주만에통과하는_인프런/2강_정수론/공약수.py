# 백준#2436 공약수(https://www.acmicpc.net/problem/2436)

# <GCD 구하는 법>
# 최대 공약수라는 말은 두 수 중 하나로 나누어서 나머지가 생기지 않는 말이다.
# 8 12
# 4 8
# 이 때 두 수 중 작은 수가 최대 공약수

# 한 수를 가능한 만큼 갭을 줄인다.
# = 하나의 수를 작은 수로 되는 만큼 뺀다는 말은
# = 나누고나서 나머지를 뜻한다.

# 121 7
# -> 121 -7 -7 -7 -7 -7 ...
# = 121%7

def _gcd(a, b):
    while(a%b != 0):
        temp = a%b
        a = b
        b = temp
    return b # 작은 수 return

def getGCD(a, b): # 다른 분 블로그 참고하다가 본 gcd 재귀함수
    if(b == 0):  return a
    return getGCD(b, a % b)


def _lcm(a, b):
    return (a*b)//_gcd(a,b)

# <백준#2436 문제풀이>
# 찾아야 하는 수를 A, B라고 뒀을 때
# A = a * gcd (이때, a,b는 서로소)
# B = b * gcd 이다. 
# lcm = a * b * gcd
# lcm / gcd = a * b 이므로 이 수(a*b)의 서로소인 약수 2개를 구하면 된다.

def solve():
    ab = int(lcm/gcd)
    result_a=0
    result_b=0

    for i in range(1, int(ab**0.5)+1): # 약수 구하기
        if(ab % i == 0): 
            a = i
            b = int(ab/i)
            if(_gcd(a,b) == 1): # 서로소인가?
                result_a = a
                result_b = b
    
    print(result_a * gcd, result_b * gcd)


gcd, lcm = map(int, input().split())

# gcd = _gcd(A, B)
# lcm = _lcm(A, B)

solve()