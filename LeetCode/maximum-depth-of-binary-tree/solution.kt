/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun maxDepth(root: TreeNode?): Int {

        fun dfs(node: TreeNode?, depth: Int): Int {

            if (node?.left == null && node?.right == null) {
                return depth
            }

            // 왼쪽 오른쪽 들어가기
            println(node.`val`)
            return maxOf(dfs(node.left, depth +1), dfs(node.right, depth +1))
        }
        
        if (root == null) {
            return 0
        }
        return dfs(root, 0) +1
    }
}
