N = int(input())
mp, mf, ms, mv = map(int, input().split())
ingre = [list(map(int, input().split())) for _ in range(N)]
answer = 99999999

use = []
used_answer = []

def recurse(index, dan, gi, tan, vi, price):
    global answer
    global use
    global used_answer

    if dan >= mp and gi >= mf and tan >= ms and vi >= mv: # 조건 만족 시 최소 비용 업데이트
            if answer > price:
                # print(answer, use)
                answer = min(answer, price)
                used_answer = []
                for i in use:
                    used_answer.append(i)
    if (index == N): # 모든 조합 사용 해봤다면
        return
    

    # 재료를 사용했을 때
    use.append(index +1)
    recurse(index+1, dan + ingre[index][0], gi+ingre[index][1], tan+ingre[index][2], vi+ingre[index][3], price + ingre[index][4])
    use.pop()

    # 재료를 사용하지 않았을 때
    recurse(index+1, dan, gi, tan, vi, price)

recurse(0, 0, 0, 0, 0, 0)
used_answer.sort()

if used_answer:
    print(answer)
    print(*used_answer)
else:
    print(-1)