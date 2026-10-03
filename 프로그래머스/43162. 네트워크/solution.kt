class Solution {
    fun solution(n: Int, computers: Array<IntArray>): Int {
        var answer = 0
        val visited = BooleanArray(n)
        
        fun dfs(node: Int): Int {
            // return 해야 하는 것
            // 이미 방문 했다면
            if (visited[node]) {
                return 0
            }
            
            visited[node] = true
            // 다음 노드 들어가기
            for (next in 0 until n) {
                if (computers[node][next] == 1)
                    dfs(next)
            }
            return 1
        }
        
        // dfs로 모든 노드 들어가되, 방문한 곳이 있다면 answer+1
        for (x in 0 until n) {
            if (dfs(x) == 1) answer+=1
        }
        
        return answer
    }
}
