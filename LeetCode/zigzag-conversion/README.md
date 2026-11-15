# 6. Zigzag Conversion

- 플랫폼: LeetCode
- 난이도: Medium
- 문제: https://leetcode.com/problems/zigzag-conversion

## 문제 설명

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

<strong>Example 1:</strong>

```
Input:s = "PAYPALISHIRING"numRows = 3Output: "PAHNAPLSIIGYIR"
```

<strong>Example 2:</strong>

```
Input:s = "PAYPALISHIRING"numRows = 4Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

<strong>Example 3:</strong>

```
Input:s = "A"numRows = 1Output: "A"
```

<strong>Constraints:</strong>

- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
- `1 <= numRows <= 1000`

출처: LeetCode, https://leetcode.com/problems/zigzag-conversion
