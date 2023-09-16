# 14568 사탕(2017 연세대학교 프로그래밍 경시대회) bronze1(https://www.acmicpc.net/problem/14568) 

candy = int(input())
cnt = 0

for 택희 in range(1, candy):
    for 영훈 in range(1, candy):
        for 남규 in range(1, candy):
            if( ((택희+영훈+남규) == candy) and (남규 >= (영훈+2)) and (택희%2 != 1)):
                cnt+=1

print(cnt)