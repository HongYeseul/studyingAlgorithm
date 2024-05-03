N = int(input())

data = [ int(input()) for _ in range(N)]

zero_cnt = [0] * 41
one_cnt = [0] * 41

zero_cnt[0] = 1
one_cnt[1] = 1

def fib(n):
    for i in range(2, n+1):
        zero_cnt[i] = zero_cnt[i-2] + zero_cnt[i-1]
        one_cnt[i] = one_cnt[i-2] + one_cnt[i-1]

for n in data:
    fib(n)
    print(zero_cnt[n], one_cnt[n])

