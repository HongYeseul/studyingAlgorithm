#16918 봄버맨 Silver1 (https://www.acmicpc.net/problem/16918)

X, Y, N = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(X) ]

# 그래프 출력 함수
def print_graph():
    for i in range(X):
        for j in range(Y):
            print(graph[i][j], end="")
        print()

def Bomb():
    global graph
    location = graph.copy() # 기존 폭탄 있던 곳은 위치 저장해두기
    graph = [ ['O']*Y for _ in range(X) ] # 폭탄으로 채우기
    for i in range(X): 
        for j in range(Y):
            if location[i][j] == 'O':
                # 상하좌우 '.'으로 치환
                graph[i][j] = '.'
                if i+1 < X: graph[i+1][j] = '.' #상
                if i > 0: graph[i-1][j] = '.' #히
                if 0 < j: graph[i][j-1] = '.' #좌
                if Y > j+1: graph[i][j+1] = '.' #우

# 0-1초: 초기상태 출력
if 0 <= N <= 1:
    print_graph()

# %2 == 0: 모든 곳에 폭탄이 있음
elif N%2 == 0:
    graph = [ ['O']*Y for _ in range(X) ]
    print_graph()


# %4 == 3: 처음 설치한 폭탄이 터진 모습
elif N%4 == 3:
    Bomb()
    print_graph()


# %4 == 1: 2번째 설치한 폭탄이 터진 모습
elif N%4 == 1:
    Bomb()
    Bomb()
    print_graph()