class Solution {
    fun islandPerimeter(grid: Array<IntArray>): Int {
        
        val visited: Array<IntArray> = Array(grid.size) { IntArray(grid[0].size) }

        fun dfs(nodeX: Int, nodeY: Int): Int {
            // 되돌아가야 하는 곳: 벽이거나 물이거나 - stripe가 생김
            if (
                (nodeX < 0 || nodeY < 0
                || nodeX >= grid.size || nodeY >= grid[0].size)
                || grid[nodeX][nodeY] == 0) {
                return 1
            }

            // 방문 했다면 PASS
            if (visited[nodeX][nodeY] == 1) {
                return 0
            }
            
            // 방문한 노드 표시
            visited[nodeX][nodeY] = 1

            // 상하좌우 방문
            return dfs(nodeX+1, nodeY) + dfs(nodeX-1, nodeY) + dfs(nodeX, nodeY-1) + dfs(nodeX, nodeY+1)
        }

        // 모든 노드를 한번씩 가보면서 땅이면 들어갔다가 return
        for (x in grid.indices) {

            for (y in grid[0].indices) {
                
                if (grid[x][y] == 1){
                    return dfs(x, y)
                }
            }
        }
        return 0
    }

}
