class Solution {
    fun solution(numbers: String): Int {
        var answer = 0
        // 1. 모든 수를 자른다
        val list = numbers.split("")
        
        // 2. 모든 수의 조합을 숫자로 만든다 => 이 때 중복이 되지 않아야 함
        val numSet = mutableSetOf<Int>()
        val visited = BooleanArray(list.size)
        
        fun dfs(next: String) {
            // 
            if (next.isNotEmpty()) {
                numSet.add(next.toInt())
            }
            // 다음 노드
            for (i in list.indices) {
                if (!visited[i]) {
                    visited[i] = true
                    val new = next + list[i]
                    dfs(new)
                    // 돌아와서 방문 해제
                    visited[i] = false
                }
            }
        }
        dfs("")
        // println(numSet.toString())
        
        // 3. 해당 숫자가 소수인지 판별한다
        fun isNumDecimal(num: Int): Boolean {
            // 1. 숫자의 제곱근까지 돌린다
            val m = Math.sqrt(num.toDouble()).toInt() +1
            
            // 2. 해당 숫자와 2이상의 배수가 존재하는지 판단
            for (i in 2 until m) {
                if (num % i == 0) {
                    return false
                }
            }
            return true
        }
        
        for (item in numSet) {
            if (item < 2) {
                continue
            }
            if (isNumDecimal(item)) {
                answer++
            }
        }
        
        return answer
    }
}
