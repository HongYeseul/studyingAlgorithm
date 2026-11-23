class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        visited = []
        result = []

        def dfs(i: int, count: int, target: int):
            if count == 0 and target == 0:
                result.append(visited.copy())
                return
            elif count < 0 or target < 0:
                return
            
            for next in range (i+1, 10):
                visited.append(next)
                dfs(next, count-1, target-next)
                visited.pop()

        dfs(0, k, n)
        return result
        
