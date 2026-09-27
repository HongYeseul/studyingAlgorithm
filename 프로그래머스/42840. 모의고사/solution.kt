class Solution {
    fun solution(answers: IntArray): IntArray {
        var answer = mutableListOf<Int>()
        
        var first = intArrayOf(1, 2, 3, 4, 5)
        var second = intArrayOf(2, 1, 2, 3, 2, 4, 2, 5)
        var third = intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
        
        var one = 0
        var two = 0
        var three = 0
        
        var idx = 0
        for (idx in 0 until answers.size) {
            
            if (first[idx % 5] == answers[idx]) {
                one++
            }
            if (second[idx % 8] == answers[idx]) {
                two++
            }
            if (third[idx % 10] == answers[idx]) {
                three++
            }
        }
        
        var m = maxOf(one, two, three)
        
        if (m == one) {
            answer.add(1)
        }
        if (m == two) {
            answer.add(2)
        }
        if (m == three) {
            answer.add(3)
        }
        
        return answer.toIntArray()
    }
}
