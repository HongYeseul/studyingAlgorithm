# 11. Container With Most Water

- 플랫폼: LeetCode
- 난이도: Medium
- 문제: https://leetcode.com/problems/container-with-most-water

## 문제 설명

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return <em>the maximum amount of water a container can store</em>.

<strong>Notice</strong> that you may not slant the container.

<strong>Example 1:</strong>

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

<strong>Example 2:</strong>

```
Input: height = [1,1]
Output: 1
```

<strong>Constraints:</strong>

- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 104`

출처: LeetCode, https://leetcode.com/problems/container-with-most-water
