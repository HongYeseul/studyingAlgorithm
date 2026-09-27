class Solution {
    fun solution(citations: IntArray): Int {
        var answer = 0
        
        // 1. 내림차순 정렬
        citations.sortDescending()
        
        // 2. answer은 citations.size보다 클 수 없으므로 모든 수를 찾아가면서 비교한다
        answer = citations.size
        for (i in answer -1 downTo 0) {
            
            citations[i]
            
            // answer 편 이상 answer 번 이상 인용 횟수가 있다
            // ==>  
            if (citations[i] >= answer) {
                return answer
            }
            
            answer--
            
        }
        
        
        return answer
    }
}
