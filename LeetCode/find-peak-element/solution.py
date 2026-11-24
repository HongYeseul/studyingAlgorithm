class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        
        low = 0
        high = len(nums)-1
        mid = 0

        while low < high:
            mid = (low + high) // 2
            if nums[mid] <= nums[mid+1]:
                # 우측이 더 큼 -> 우측 한칸 이동
                low = mid +1
            # 좌측이 더 큼 -> 좌측 버림
            else:
                high = mid

        return low
