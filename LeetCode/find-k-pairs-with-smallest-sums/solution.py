import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        # 최소 힙 우선순위 큐        
        result = []
        heap = []

        # 비교할 후보 준비
        for i in range( min(len(nums1), k) ):
            heapq.heappush(heap, (nums1[i]+nums2[0], i, 0))
        
        while heap and len(result) < k:
            total, x, y = heapq.heappop(heap)
            result.append([nums1[x], nums2[y]])

            # 꺼낸 다음 쌍만 새 후보로 추가
            if y + 1 < len(nums2):
                n = nums1[x] + nums2[y+1], x, y+1
                heapq.heappush(heap, n)

        # .. 어렵다 이 문제
        return result
