N = int(input())
interview = [list(map(int, input().split())) for _ in range(N)]

answer = 0
def recurse(date, price):
    global answer
    # 상담이 딱 맞게 이뤄 졌다면
    if date == N:
        answer = max(answer, price)
        return

    # 모든 상담 조합을 봤다면
    if date > N - 1:
        return

    # 상담을 잡았을 때
    recurse(date + interview[date][0], price + interview[date][1])

    # 상담을 잡지 않았을 때
    recurse(date+1, price)

recurse(0,0)
print(answer)