class Solution:
    def canJump(self, nums: list[int]) -> bool:
        
        # 최대로 갈 수 있는 index 저장용
        farthest: int = 0

        for i in range(len(nums)):

            # 실패 조건: 지금 칸 i가 도달 가능한 구간 밖에 있음
            if i > farthest:
                return False
            
            farthest = max(farthest, i + nums[i])

            if farthest >= len(nums)-1:
                return True

        return False
