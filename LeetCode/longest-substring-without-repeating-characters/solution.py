class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_ = set()

        left = 0
        right = 1
        max_len = 0

        if (len(s) <= 1):
            return len(s)

        while (right < len(s)):
            set_.add(s[left])

            while (s[right] in set_):
                set_.remove(s[left])
                left+=1
            set_.add(s[right])

            if (max_len < len(set_)):
                max_len = len(set_)

            right+=1

        return max_len
