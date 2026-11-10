# 57. Insert Interval

- 플랫폼: LeetCode
- 난이도: Medium
- 문제: https://leetcode.com/problems/insert-interval

## 문제 설명

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the `ith` interval and `intervals` is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Two intervals are considered overlapping if they share <strong>at least</strong> one point.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` <em>after the insertion</em>.

<strong>Note</strong> that you don't need to modify `intervals` in-place. You can make a new array and return it.

<strong>Example 1:</strong>

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

<strong>Example 2:</strong>

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

<strong>Constraints:</strong>

- `0 <= intervals.length <= 104`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 105`
- `intervals` is sorted by `starti` in <strong>ascending</strong> order.
- `newInterval.length == 2`
- `0 <= start <= end <= 105`

출처: LeetCode, https://leetcode.com/problems/insert-interval
