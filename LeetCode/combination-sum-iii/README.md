# 216. Combination Sum III

- 플랫폼: LeetCode
- 난이도: Medium
- 문제: https://leetcode.com/problems/combination-sum-iii

## 문제 설명

Find all valid combinations of `k` numbers that sum up to `n` such that the following conditions are true:

- Only numbers `1` through `9` are used.
- Each number is used <strong>at most once</strong>.

Return <em>a list of all possible valid combinations</em>. The list must not contain the same combination twice, and the combinations may be returned in any order.

<strong>Example 1:</strong>

```
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
```

<strong>Example 2:</strong>

```
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
```

<strong>Example 3:</strong>

```
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
```

<strong>Constraints:</strong>

- `2 <= k <= 9`
- `1 <= n <= 60`

출처: LeetCode, https://leetcode.com/problems/combination-sum-iii
