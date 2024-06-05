import sys
sys.setrecursionlimit(1000000)
N, M = map(int, sys.stdin.readline().split())

# 자기 자신을 가리키도록 부모노드 초기화
parent = [i for i in range(N+1)]

# # 랭크 초기화
# rank = [0 for _ in range(N+1)]

############################

# find: 찾기
# _find 최적화 하는 법 = 경로 단축
def _find(A):
    if A != parent[A]:  # 만약에 스스로를 부모로 칭하고 있지 않다면
        parent[A] = _find(parent[A]) # 부모를 루트로 갱신
    return parent[A]

# union: 집합
# _union 최적화 하는 방법 = union by rank(랭크를 두고 합치는 것)
# 트리의 높이를 최소화하도록 랭크를 사용한다.
# 동일한 랭크를 가진 두 트리를 합칠 때만 랭크를 증가 시킨다.
def _union(A, B): # 최대 높이를 확인해서 합쳐줌
    rootA = _find(A)
    rootB = _find(B)

    if rootA < rootB: # 값이 더 작은 쪽을 부모로
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

    # if rootA != rootB:
    #     if rank[rootA] > rank[rootB]:
    #         parent[rootB] = rootA
    #     elif rank[rootA] < rank[rootB]:
    #         parent[rootA] = rootB
    #     else: # 높이가 동일하니까 반대로 해도 상관없음
    #         parent[rootB] = rootA
    #         rank[rootA] += 1

############################

for _ in range(M):
    X, A, B = map(int, sys.stdin.readline().split())

    if X == 0: # 합집합 연산(A가 B의 부모가 된다)
        _union(A, B)
    else: # 찾기 연산
        if _find(A) == _find(B):
            print("YES")
        else:
            print("NO")