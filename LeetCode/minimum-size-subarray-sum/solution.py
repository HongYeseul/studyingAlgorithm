class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        sumArr = [0] * (len(nums)+1)

        minSize = len(nums) + 1
        start = 0
        end = 0

        # 누적합 배열 만들기
        for i in range(len(nums)):
            sumArr[i+1] = sumArr[i] + nums[i]

        while start <= end and end <= len(nums):
            minus = sumArr[end] - sumArr[start]

            # print(">>", start, end, minus)
            if target <= minus:
                size = end-start
                if minSize > size:
                    minSize = size

            if target <= minus:
                start += 1
            else: # target >= minus
                end += 1
        
        # print(start, end, minSize)
        # print(sumArr)

        if minSize == len(nums) + 1:
            return 0

        return minSize
