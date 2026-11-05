from collections import deque

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = [False] * n

        # 처음 노드 방문 처리
        q = deque([source])

        # q가 존재할 때까지
        while q:
            this = q.popleft()

            if this == destination:
                return True
            
            # 다음 노드
            for x in graph[this]:

                if not visited[x]:
                    q.append(x)
                    visited[x] = True

        return False
