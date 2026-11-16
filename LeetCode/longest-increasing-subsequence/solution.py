class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # 앞에 존재하는 dp 수열 뒤 하나를 붙이는 것과 비교
                    dp[i] = max(dp[i], dp[j] +1)

        return max(dp)
