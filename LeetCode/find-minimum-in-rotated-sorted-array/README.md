# 153. Find Minimum in Rotated Sorted Array

- 플랫폼: LeetCode
- 난이도: Medium
- 문제: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

## 문제 설명

Suppose an array of length `n` sorted in ascending order is <strong>rotated</strong> between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that <strong>rotating</strong> an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of <strong>unique</strong> elements, return <em>the minimum element of this array</em>.

You must write an algorithm that runs in `O(log n) time`.

<strong>Example 1:</strong>

```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

<strong>Example 2:</strong>

```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

<strong>Example 3:</strong>

```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

<strong>Constraints:</strong>

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are <strong>unique</strong>.
- `nums` is sorted and rotated between `1` and `n` times.

출처: LeetCode, https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
