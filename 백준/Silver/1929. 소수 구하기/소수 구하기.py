import sys
M, N = map(int, sys.stdin.readline().split())


# 에라토스테네스의 체
def get_primes(N):
    # 0, 1은 소수가 아니므로 False로 초기화
    is_prime = [False, False] + [True] * (N - 1)
    primes = []
    for i in range(2, N+1):
        if is_prime[i]:
            primes.append(i)
            # i의 배수들을 모두 소수가 아닌 것으로 표시
            for j in range(i*2, N+1, i):
                is_prime[j] = False
    return primes

primes = get_primes(N)

for p in primes:
    if p >= M:
        print(p)