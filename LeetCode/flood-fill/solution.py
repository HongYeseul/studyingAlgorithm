from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # 시작 세팅
        visited = [[False] * len(image[0]) for _ in range(len(image))]

        # start node 방문
        queue = deque([(sr, sc)])
        targetColor = image[sr][sc]
        image[sr][sc] = color
        visited[sr][sc] = True

        # while 큐가 빌 때까지
        while queue:
            # 노드 꺼내기
            (x, y) = queue.popleft()
            # print(x, y)

            # 방문 표시, 다음 노드 넣기
            # 상하좌우
            if x < len(image) -1:
                if not visited[x+1][y] and image[x+1][y] == targetColor:
                    queue.append((x +1, y))
                    visited[x+1][y] = True
                    image[x+1][y] = color
                    
            if y < len(image[0]) -1:
                if not visited[x][y+1] and image[x][y+1] == targetColor:
                    queue.append((x, y+1))
                    visited[x][y+1] = True
                    image[x][y+1] = color

            if x > 0:
                if not visited[x-1][y] and image[x-1][y] == targetColor:
                    queue.append((x-1, y))
                    visited[x-1][y] = True
                    image[x-1][y] = color

            if y > 0:
                if not visited[x][y-1] and image[x][y-1] == targetColor:
                    queue.append((x, y-1))
                    visited[x][y-1] = True
                    image[x][y-1] = color

        # print(visited)
        return image
