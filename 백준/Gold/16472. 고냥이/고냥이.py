import sys

N = int(sys.stdin.readline())
data = list(sys.stdin.readline().rstrip())

start = 0
max_length = 0
# char 개수를 담아두는 dictionary 생성
char_cnt = {}

for end in range(len(data)):
    if data[end] in char_cnt:
        char_cnt[data[end]] += 1
    else:
        char_cnt[data[end]] = 1
    
    # 윈도우 내 알파벳 종류가 N을 초과하면 left 포인터 이동
    while len(char_cnt) > N:
        char_cnt[data[start]] -= 1
        if char_cnt[data[start]] == 0:
            del char_cnt[data[start]]
        start += 1
    
    # 최대 길이 갱신
    max_length = max(max_length, end - start +1)

print(max_length)