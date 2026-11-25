# 189. Rotate Array

- 플랫폼: LeetCode
- 난이도: Medium
- 문제: https://leetcode.com/problems/rotate-array

## 문제 설명

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

<strong>Example 1:</strong>

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

<strong>Example 2:</strong>

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

<strong>Constraints:</strong>

- `1 <= nums.length <= 105`
- `-231 <= nums[i] <= 231 - 1`
- `0 <= k <= 105`

<strong>Follow up:</strong>

- Try to come up with as many solutions as you can. There are at least <strong>three</strong> different ways to solve this problem.
- Could you do it in-place with `O(1)` extra space?

출처: LeetCode, https://leetcode.com/problems/rotate-array
