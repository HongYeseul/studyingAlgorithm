class Solution {
    fun search(nums: IntArray, target: Int): Int {
        
        var low = 0
        var high = nums.size -1

        while (low <= high) {

            var mid = (low + high) / 2

            if (nums[mid] == target) {
                return mid
            }

            // 왼쪽 구간이 정렬 됨
            if (nums[low] <= nums[mid]) {
                // target이 mid 기준 좌측에 있을 때
                if (nums[mid] > target && nums[low] <= target) {
                    high = mid -1
                }
                else { // target이 좌측에 없을 때
                    low = mid + 1
                }
            }
            else { // 우측 구간이 정렬된 경우
                // target이 mid 기준 우측에 있을 때
                if (nums[mid] < target && nums[high] >= target) {
                    low = mid + 1
                }
                else { // target이 우측에 없을 때 
                    high = mid - 1
                }
            }
        }

        return -1
    }
}
