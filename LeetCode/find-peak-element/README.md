# 162. Find Peak Element

- 플랫폼: LeetCode
- 난이도: Medium
- 문제: https://leetcode.com/problems/find-peak-element

## 문제 설명

A peak element is an element that is strictly greater than its neighbors.

Given a <strong>0-indexed</strong> integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to <strong>any of the peaks</strong>.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

<strong>Example 1:</strong>

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

<strong>Example 2:</strong>

```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

<strong>Constraints:</strong>

- `1 <= nums.length <= 1000`
- `-231 <= nums[i] <= 231 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.

출처: LeetCode, https://leetcode.com/problems/find-peak-element
