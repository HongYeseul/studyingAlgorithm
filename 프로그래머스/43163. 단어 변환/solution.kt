class Solution {
    fun solution(begin: String, target: String, words: Array<String>): Int {
        var answer = 0
        var visited = BooleanArray(words.size)
        
        // 모든 단어를 보면서 다음 단어와 한 글자가 다르면 변환 해본다
        fun dfs(node: Int, count: Int): Int {
            // return 조건
            if (visited[node]) {
                return 0
            }
            // 정답일 때
            if (words[node] == target) {
                return count +1
            }
            
            visited[node] = true
            // println("${words[node]}, $count")
            var best = 0
            // 다음 단어 찾아보기
            for (next in 0 until words.size) {
                val diffrentCount = begin.indices.count { words[node][it] != words[next][it] }
                if (diffrentCount == 1) {
                    val result = dfs(next, count+1)
                    if (result > 0 && (best == 0 || result < best))
                        best = result
                }
            }
            return best
        }
        
        for (node in words.indices) {
            visited.fill(false)
            
            val diffrentCount = begin.indices.count { begin[it] != words[node][it] }
            if (diffrentCount == 1) {
                val result = dfs(node, 0)
                if (result > 0 && (answer == 0 || result < answer))
                    answer = result
            }
        }
        
        return answer
    }
}
