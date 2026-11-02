# 1732. Find the Highest Altitude

- 플랫폼: LeetCode
- 난이도: Easy
- 문제: https://leetcode.com/problems/find-the-highest-altitude

## 문제 설명

There is a biker going on a road trip. The road trip consists of `n + 1` points at various altitudes. The biker starts his trip on point `0` with altitude equal `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the <strong>net gain in altitude</strong> between points `i`​​​​​​ and `i + 1` for all (`0 <= i < n)`. Return <em>the <strong>highest altitude</strong> of a point.</em>

<strong>Example 1:</strong>

```
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
```

<strong>Example 2:</strong>

```
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
```

<strong>Constraints:</strong>

- `n == gain.length`
- `1 <= n <= 100`
- `-100 <= gain[i] <= 100`

출처: LeetCode, https://leetcode.com/problems/find-the-highest-altitude
