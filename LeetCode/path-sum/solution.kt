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
    fun hasPathSum(root: TreeNode?, targetSum: Int): Boolean {
        
        var isTrue:Boolean = false
        fun dfs(node: TreeNode?, sum: Int) {

            // return 되는 조건
            if (node == null) return

            if (node.left == null && node.right == null) {
                if (sum + node.`val` == targetSum) isTrue = true
                return
            }

            // 다음 노드 - 왼쪽 / 오른쪽
            if (node.left != null) {
                dfs(node.left, sum + node.`val`)
            }
            if (node.right != null) {
                dfs(node.right, sum + node.`val`)
            }
        }

        dfs(root, 0)
        return isTrue
    }
}
