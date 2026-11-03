# 98. Validate Binary Search Tree

- 플랫폼: LeetCode
- 난이도: Medium
- 문제: https://leetcode.com/problems/validate-binary-search-tree

## 문제 설명

Given the `root` of a binary tree, <em>determine if it is a valid binary search tree (BST)</em>.

A <strong>valid BST</strong> is defined as follows:

- The left of a node contains only nodes with keys <strong>strictly less than</strong> the node's key.
- The right subtree of a node contains only nodes with keys <strong>strictly greater than</strong> the node's key.
- Both the left and right subtrees must also be binary search trees.

<strong>Example 1:</strong>

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

```
Input: root = [2,1,3]
Output: true
```

<strong>Example 2:</strong>

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

<strong>Constraints:</strong>

- The number of nodes in the tree is in the range `[1, 104]`.
- `-231 <= Node.val <= 231 - 1`

출처: LeetCode, https://leetcode.com/problems/validate-binary-search-tree
