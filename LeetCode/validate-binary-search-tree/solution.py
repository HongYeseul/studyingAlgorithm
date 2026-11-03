# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        
        def dfs(node: TreeNode, low: int, high: int) -> int:
            # return 조건
            # 왼 오 둘다 null이면 leaf node
            if node == None:
                return 0
            
            # 현재 값이 허용 범위 내에 있어야 함
            if not (low < node.val < high):
                return -1

            # 다음 노드, 왼쪽이면 상한이 현재 노드값, 우측이면 하한이 현재 노드값
            return dfs(node.left, low, node.val) + dfs(node.right, node.val, high)
        
        if (dfs(root, float('-inf'), float('inf')) < 0):
            return False
        return True
