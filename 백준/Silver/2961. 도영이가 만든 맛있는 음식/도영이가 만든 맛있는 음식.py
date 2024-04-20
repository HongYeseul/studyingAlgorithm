import sys
N = int(sys.stdin.readline())
ingre = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 99999999

def recurse(index, s, b, use):
    global answer
    
    if (index == N): # 모든 재료 사용
        if (use == 0): # 아무것도 사용 안했을 때 
            return
        answer = min(answer, abs(s - b))
        return

    # 재료를 사용했을 때
    recurse(index+1, s*ingre[index][0], b+ingre[index][1], use+1)

    # 재료를 사용하지 않았을 때
    recurse(index+1, s, b, use)

recurse(0, 1, 0, 0)
print(answer)