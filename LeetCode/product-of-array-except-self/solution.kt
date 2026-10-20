class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        
        // 투포인터 사용하기
        val a = IntArray(nums.size) {1}
        val b = IntArray(nums.size) {1}

        a[0] = nums[0]
        for (i in 1 until nums.size) {
            a[i] = a[i-1]*nums[i]
        }

        b[nums.size-1] = nums[nums.size-1]
        for (i in nums.size-2 downTo 0) {
            b[i] = b[i+1]*nums[i]
        }
        val result = IntArray(nums.size) { 1 }

        println(a.contentToString())
        println(b.contentToString())

        for (i in 0 until nums.size) {
            if (i == 0) {
                result[i] = b[i+1]
                continue
            }
            if (i == nums.size-1) {
                result[i] = a[i-1]
                continue
            }
            result[i] = a[i-1] * b[i+1]
        }
        return result
    }
}
