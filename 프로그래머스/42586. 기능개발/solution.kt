class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var answer = mutableListOf<Int>()
        val days = IntArray(progresses.size) { i -> 
            // 각 기능이 얼마나 걸리는지 계산
            (100 - progresses[i] + speeds[i] -1) / speeds[i]
        }
        
        
        var start = days[0]
        var count = 0
        for (n in days) {
            
            if (start >= n) {
                count+=1
            } else {
                answer.add(count)
                count = 1
                start = n
            }
            
        }
        answer.add(count)
        
        return answer.toIntArray()
    }
}
