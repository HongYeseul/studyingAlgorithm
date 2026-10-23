class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        
        val visited = Array(grid.size) { BooleanArray(grid[0].size) }
        var cnt:Int = 0

        fun dfs(x: Int, y: Int) {

            if (y < 0 || y > grid[0].size-1 || x < 0 || x > grid.size-1) {
                return
            }
            // 방문 했었다면 return
            if (visited[x][y]) {
                return
            }
            // 물을 만난다면 return
            if (grid[x][y] == '0') {
                return
            }

            visited[x][y] = true

            // 다음 칸 찾아가기
            // 왼/오/위/아래
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
        }

        for (i in 0 until grid.size) {

            for (j in 0 until grid[0].size) {
                // 방문하지 않은 '땅'
                if (!visited[i][j] && grid[i][j] == '1') {
                    cnt++
                    dfs(i, j)
                }
            }
        }

        return cnt
    }
}
