class Solution {
    fun floodFill(image: Array<IntArray>, sr: Int, sc: Int, color: Int): Array<IntArray> {

        var visited: Array<BooleanArray> = Array(image.size) { BooleanArray(image[0].size) }

        var startColor = image[sr][sc]
        fun dfs(nodeX: Int, nodeY: Int) {

            // 만약 벽이거나 다른 색상을 만난다면 return
            if ((nodeX < 0 || nodeY < 0 || nodeX >= image.size || nodeY >= image[0].size) || image[nodeX][nodeY] != startColor) {
                return
            }

            // 만약 왔었던 node라면 return
            if (visited[nodeX][nodeY] == true) return

            // 컬러 색칠
            image[nodeX][nodeY] = color
            // visited
            visited[nodeX][nodeY] = true

            // 상하좌우 확인
            dfs(nodeX +1, nodeY)
            dfs(nodeX -1, nodeY )
            dfs(nodeX, nodeY-1)
            dfs(nodeX, nodeY+1)
        }

        dfs(sr, sc)
        return image
    }
}
