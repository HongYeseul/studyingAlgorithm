class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 내일 다시 볼 것
        result = 0
        current_sum = 0

        sum_counts = {}
        sum_counts[0] = 1

        for num in nums:
            current_sum = current_sum + num

            previous_sum = current_sum - k

            if previous_sum in sum_counts:
                matching_count = sum_counts[previous_sum]
                result = result + matching_count

            if current_sum in sum_counts:
                sum_counts[current_sum] = sum_counts[current_sum] + 1
            else:
                sum_counts[current_sum] = 1

        return result
