# 1971. Find if Path Exists in Graph

- 플랫폼: LeetCode
- 난이도: Easy
- 문제: https://leetcode.com/problems/find-if-path-exists-in-graph

## 문제 설명

There is a <strong>bi-directional</strong> graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (<strong>inclusive</strong>). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [ui, vi]` denotes a bi-directional edge between vertex `ui` and vertex `vi`. Every vertex pair is connected by <strong>at most one</strong> edge, and no vertex has an edge to itself.

You want to determine if there is a <strong>valid path</strong> that exists from vertex `source` to vertex `destination`.

Given `edges` and the integers `n`, `source`, and `destination`, return `true` <em>if there is a <strong>valid path</strong> from</em> `source` <em>to</em> `destination`<em>, or</em> `false` <em>otherwise</em><em>.</em>

<strong>Example 1:</strong>

![](https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png)

```
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
```

<strong>Example 2:</strong>

![](https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png)

```
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
```

<strong>Constraints:</strong>

- `1 <= n <= 2 * 105`
- `0 <= edges.length <= 2 * 105`
- `edges[i].length == 2`
- `0 <= ui, vi <= n - 1`
- `ui != vi`
- `0 <= source, destination <= n - 1`
- There are no duplicate edges.
- There are no self edges.

출처: LeetCode, https://leetcode.com/problems/find-if-path-exists-in-graph
