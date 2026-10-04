class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var answer = mutableListOf<Int>()
        var days = IntArray(progresses.size)
        
        for (i in 0 until progresses.size) {
            
            // 필요한 날짜 세기
            var d = (100 - progresses[i]) / speeds[i]
            if ((100 - progresses[i]) % speeds[i] > 0) d+=1
            
            days[i] = d
            
        }
        
        // println(days.contentToString())
        
        var start = days[0]
        var count = 0
        for (i in 0 until progresses.size) {
            // println("start: $start count: $count answer $answer")
            
            if (start >= days[i]) {
                count+=1
            } else {
                answer.add(count)
                count = 1
                start = days[i]
            }
        }
        answer.add(count)
        
        return answer.toIntArray()
    }
}
