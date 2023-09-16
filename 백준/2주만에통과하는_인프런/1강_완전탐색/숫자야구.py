#2503 숫자야구 Silver3 (https://www.acmicpc.net/problem/2503)

n = int(input())

x = []
y = []
z = []
strike = []
ball = []

for i in range(n):
    temp, str, b = map(int, input().split())
    strike.append(str)
    ball.append(b)
    x.append(int(temp/100))
    temp= temp%100
    y.append(int(temp/10))
    temp = temp%10
    z.append(temp)

result=0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10): #3자리수 계산

            if i==j or j==k or i==k: continue # 주의! 문제에서 생각되는 숫자는 '서로다른 숫자' 3개이다.
            cnt=0

            for t in range(n): # 입력 받은 경우의 수와 대조하기
                s=0
                b=0

                # strike 개수 세기
                if i == x[t]: s+=1
                if j == y[t]: s+=1
                if k == z[t]: s+=1
                
                # ball 개수 세기
                if (i==y[t] or i==z[t]): b+=1
                if (j==x[t] or j==z[t]): b+=1
                if (k==x[t] or k==y[t]): b+=1

                if( s==strike[t] and b==ball[t]): cnt+=1

            if(cnt == n): result+=1

print(result)