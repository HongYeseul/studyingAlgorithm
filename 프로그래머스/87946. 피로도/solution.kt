class Solution {
    fun solution(k: Int, dungeons: Array<IntArray>): Int {
        var answer: Int = -1
        var health = k
        
        // 모든 순서 방문하기 - 백트래킹 / DP
        var visited = BooleanArray(dungeons.size)
        var maxCount = 0
        // 방문 했을 때 최대 탐험 횟수 반환
        fun dfs(node: Int): Int {
            
            // return 조건
            if (visited[node]) {
                return 0
            }
            // 던전 수치 계산
            if (health < dungeons[node][0]) {
                return 0
            }
            
            // 방문 기록
            visited[node] = true
            health -= dungeons[node][1]
            maxCount++
            
            // 다음 노드 방문
            var n = 0
            for (next in dungeons.indices) {
                // maxOf(dfs(next), maxCount)
                n = maxOf(dfs(next), n)
            }
            // 방문 후
            visited[node] = false
            health += dungeons[node][1]
            
            return maxOf(n, maxCount--)
        }
        
        var m = 0
        for (n in dungeons.indices) {
            visited.fill(false)
            health = k
            val result = dfs(n)
            // println("n: $n result: $result, maxCount: $maxCount")
            m = maxOf(m, result)
        }
        
        return m
    }
}
