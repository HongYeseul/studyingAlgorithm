class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        left = 0
        right = len(height) -1
        maxWater = 0

        while (left < right):
            # 현재의 물의 양 구하기
            
            a = right - left # 가로
            b = min(height[left], height[right]) # 세로
            water = a * b
            maxWater = max(maxWater, water)

            # 왼 < 오 -> 왼쪽을 오른쪽으로 이동
            if height[left] < height[right]:
                left += 1
            elif right > 0:
                right -= 1
        
        return maxWater
