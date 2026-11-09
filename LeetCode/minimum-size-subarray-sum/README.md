# 209. Minimum Size Subarray Sum

- 플랫폼: LeetCode
- 난이도: Medium
- 문제: https://leetcode.com/problems/minimum-size-subarray-sum

## 문제 설명

Given an array of positive integers `nums` and a positive integer `target`, return <em>the <strong>minimal length</strong> of a</em> <em>whose sum is greater than or equal to</em> `target`. If there is no such subarray, return `0` instead.

<strong>Example 1:</strong>

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

<strong>Example 2:</strong>

```
Input: target = 4, nums = [1,4,4]
Output: 1
```

<strong>Example 3:</strong>

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

<strong>Constraints:</strong>

- `1 <= target <= 109`
- `1 <= nums.length <= 105`
- `1 <= nums[i] <= 104`

<strong>Follow up:</strong> If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

출처: LeetCode, https://leetcode.com/problems/minimum-size-subarray-sum
