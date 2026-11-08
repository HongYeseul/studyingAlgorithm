class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        def binarySearch(start: int, end: int) -> int:
            while start <= end:
                mid = (start+end) // 2

                if start == end:
                    return start

                # mid < end 최소가 좌측에 존재
                if nums[mid] < nums[end]:
                    end = mid
                elif nums[mid] > nums[end]:
                    # mid > end 최소가 우측에 존재 
                    start = mid +1
            
            return mid

        
        mid = len(nums)//2
        end = len(nums)-1
        n = 0
        print(nums[mid], nums[end])
        # mid < end 최소가 좌측에 존재
        if nums[mid-1] < nums[end]:
            n = binarySearch(0, mid)
        else: # mid > end 최소가 우측에 존재
            n = binarySearch(mid, end)

        return nums[n]
