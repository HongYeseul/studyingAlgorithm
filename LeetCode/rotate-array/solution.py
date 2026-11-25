from collections import deque

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dq = deque(nums)

        for i in range (0,k):
            n = dq.pop()
            dq.appendleft(n)
        
        nums[:] = list(dq)
