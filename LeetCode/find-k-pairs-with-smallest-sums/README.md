# 373. Find K Pairs with Smallest Sums

- 플랫폼: LeetCode
- 난이도: Medium
- 문제: https://leetcode.com/problems/find-k-pairs-with-smallest-sums

## 문제 설명

You are given two integer arrays `nums1` and `nums2` sorted in <strong>non-decreasing order</strong> and an integer `k`.

Define a pair `(u, v)` which consists of one element from the first array and one element from the second array.

Return <em>the</em> `k` <em>pairs</em> `(u1, v1), (u2, v2), ..., (uk, vk)` <em>with the smallest sums</em>.

<strong>Example 1:</strong>

```
Input:nums1 = [1, 7, 11]nums2 = [2, 4, 6]k = 3Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```

<strong>Example 2:</strong>

```
Input:nums1 = [1, 1, 2]nums2 = [1, 2, 3]k = 2Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
```

<strong>Constraints:</strong>

- `1 <= nums1.length, nums2.length <= 105`
- `-109 <= nums1[i], nums2[i] <= 109`
- `nums1` and `nums2` both are sorted in <strong>non-decreasing order</strong>.
- `1 <= k <= 104`
- `k <= nums1.length * nums2.length`

출처: LeetCode, https://leetcode.com/problems/find-k-pairs-with-smallest-sums
