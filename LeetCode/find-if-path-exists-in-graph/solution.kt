class Solution {
    fun validPath(n: Int, edges: Array<IntArray>, source: Int, destination: Int): Boolean {
        
        val visited = BooleanArray(n)
        val graph = Array(n) { mutableListOf<Int>() }

        // 양방향 그래프 그리기
        for ((a, b) in edges) {
            graph[a].add(b)
            graph[b].add(a)
        }

        // dfs: 한 곳에서 시작해서 모든 노드를 갈 수 있는지
        var isDestination: Boolean = false
        fun dfs(node: Int) {

            // 만약 visited 한 노드라면 return
            if (visited[node]) {
                return
            }
            // 만약 destination에 도달했다면 return
            if (node == destination) {
                isDestination = true
                return
            }

            visited[node] = true
            // 들어가기 - 연결된 노드 전부
            for (next in graph[node]) {
                dfs(next)
            }
        }

        dfs(source)
        return isDestination
    }
}
