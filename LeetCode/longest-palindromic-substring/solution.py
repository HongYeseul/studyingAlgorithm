class Solution:
    def longestPalindrome(self, s: str) -> str:
        strArr = list(s)

        def isPalindrome(arr: []) -> bool:
            left = 0
            right = len(arr)-1

            while left < right:
                if arr[left] != arr[right]:
                    return False
                left+=1
                right-=1
            
            return True
        

        for x in range(len(strArr), 0, -1):
            left = 0
            right = x
            
            # 모든 사이즈(right - left)만큼 순차 검사 
            while right <= len(strArr):
                if (isPalindrome(strArr[left:right])):
                    return "".join(strArr[left:right])
                
                left += 1
                right += 1
        
        return strArr[0]
