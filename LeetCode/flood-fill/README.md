# 733. Flood Fill

- 플랫폼: LeetCode
- 난이도: Easy
- 문제: https://leetcode.com/problems/flood-fill

## 문제 설명

You are given an image represented by an `m x n` grid of integers `image`, where `image[i][j]` represents the pixel value of the image. You are also given three integers `sr`, `sc`, and `color`. Your task is to perform a <strong>flood fill</strong> on the image starting from the pixel `image[sr][sc]`.

To perform a <strong>flood fill</strong>:

1. Begin with the starting pixel and change its color to `color`.
2. Perform the same process for each pixel that is <strong>directly adjacent</strong> (pixels that share a side with the original pixel, either horizontally or vertically) and shares the <strong>same color</strong> as the starting pixel.
3. Keep <strong>repeating</strong> this process by checking neighboring pixels of the <em>updated</em> pixels and modifying their color if it matches the original color of the starting pixel.
4. The process <strong>stops</strong> when there are <strong>no more</strong> adjacent pixels of the original color to update.

Return the <strong>modified</strong> image after performing the flood fill.

<strong>Example 1:</strong>

<strong>Input:</strong> image = \[\[1,1,1\],\[1,1,0\],\[1,0,1\]\], sr = 1, sc = 1, color = 2

<strong>Output:</strong> \[\[2,2,2\],\[2,2,0\],\[2,0,1\]\]

<strong>Explanation:</strong>

![](https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg)

From the center of the image with position `(sr, sc) = (1, 1)` (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is <strong>not</strong> colored 2, because it is not horizontally or vertically connected to the starting pixel.

<strong>Example 2:</strong>

<strong>Input:</strong> image = \[\[0,0,0\],\[0,0,0\]\], sr = 0, sc = 0, color = 0

<strong>Output:</strong> \[\[0,0,0\],\[0,0,0\]\]

<strong>Explanation:</strong>

The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

<strong>Constraints:</strong>

- `m == image.length`
- `n == image[i].length`
- `1 <= m, n <= 50`
- `0 <= image[i][j], color < 216`
- `0 <= sr < m`
- `0 <= sc < n`

출처: LeetCode, https://leetcode.com/problems/flood-fill
