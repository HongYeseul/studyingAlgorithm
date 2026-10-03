class Solution {
    fun solution(n: Int, computers: Array<IntArray>): Int {
        var answer = 0
        var visited = BooleanArray(n+1)
        
        // 연결 된 곳 표시
        var graph = Array(n+1) { mutableListOf<Int>() }
        for (i in 0 until n) {
            for (j in computers[i].indices) {
                
                if (i!=j && computers[i][j] == 1) {
                    graph[i].add(j+1)
                    graph[j].add(i+1)
                }
                
            }
            // println(graph[i])
        }
        
        var sum = 0
        fun dfs(node: Int) {
            // return 해야 하는 것
            // 이미 방문 했다면
            if (visited[node] == true) {
                return
            }
            
            visited[node] = true
            sum+=1
            // 다음 노드 들어가기
            for (next in graph[node-1]) {
                dfs(next)
            }
        }
        
        // dfs로 모든 노드 들어가되, n개 만큼 sum값이 안되면 다음 네트워크
        for (x in 1 until n+1) {
            sum = 0
            dfs(x)
            
            if (sum != 0) answer+=1
            if (sum == n) return 1
        }
        
        
        return answer
    }
}
