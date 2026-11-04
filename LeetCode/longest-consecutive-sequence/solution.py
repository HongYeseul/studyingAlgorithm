class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        s = sorted(set(nums))

        result = 0
        cnt = 1
        max_num = s[0]
        for idx in range(1, len(s)):
            # print(max_num, s[idx])
            if (max_num +1) == s[idx]:
                max_num = s[idx]
                cnt+=1
            
            else:
                # print("else: ", idx, result, cnt, max_num)
                if (result < cnt):
                    result = cnt
                cnt = 1
                max_num = s[idx]
        
        if (cnt > result):
            return cnt
        return result
