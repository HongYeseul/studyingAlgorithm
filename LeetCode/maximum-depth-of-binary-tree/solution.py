# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        
        # 시작 노드
        result = 0
        q = deque([root]) if root is not None else deque()

        # 큐가 빌 때까지
        while q:
            # 방문 처리
            # print("Queue size", len(q))
            # print(q)
            count = len(q)

            # 큐의 개수만큼
            for _ in range(count):
                node = q.popleft()

                # 다음 노드 방문
                if node.left is not None:
                    q.append(node.left)
                    
                if node.right is not None:
                    q.append(node.right)
            
            result += 1

        return result
