class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotate = k % len(nums)
        if rotate == 0 or len(nums) <= 1:
            return
        nums[:] = nums[len(nums)-rotate:] + nums[:-rotate]
