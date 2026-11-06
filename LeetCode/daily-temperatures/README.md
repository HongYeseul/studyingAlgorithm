# 739. Daily Temperatures

- 플랫폼: LeetCode
- 난이도: Medium
- 문제: https://leetcode.com/problems/daily-temperatures

## 문제 설명

Given an array of integers `temperatures` represents the daily temperatures, return <em>an array</em> `answer` <em>such that</em> `answer[i]` <em>is the number of days you have to wait after the</em> `ith` <em>day to get a warmer temperature</em>. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

<strong>Example 1:</strong>

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

<strong>Example 2:</strong>

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

<strong>Example 3:</strong>

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

<strong>Constraints:</strong>

- `1 <= temperatures.length <= 105`
- `30 <= temperatures[i] <= 100`

출처: LeetCode, https://leetcode.com/problems/daily-temperatures
