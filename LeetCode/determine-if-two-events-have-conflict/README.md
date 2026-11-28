# 2446. Determine if Two Events Have Conflict

- 플랫폼: LeetCode
- 난이도: Easy
- 문제: https://leetcode.com/problems/determine-if-two-events-have-conflict

## 문제 설명

You are given two arrays of strings that represent two inclusive events that happened <strong>on the same day</strong>, `event1` and `event2`, where:

- `event1 = [startTime1, endTime1]` and
- `event2 = [startTime2, endTime2]`.

Event times are valid 24 hours format in the form of `HH:MM`.

A <strong>conflict</strong> happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return `true` <em>if there is a conflict between two events. Otherwise, return</em> `false`.

<strong>Example 1:</strong>

```
Input:event1 = ["01:15", "02:00"]event2 = ["02:00", "03:00"]Output: true
Explanation: The two events intersect at time 2:00.
```

<strong>Example 2:</strong>

```
Input:event1 = ["01:00", "02:00"]event2 = ["01:20", "03:00"]Output: true
Explanation: The two events intersect starting from 01:20 to 02:00.
```

<strong>Example 3:</strong>

```
Input:event1 = ["10:00", "11:00"]event2 = ["14:00", "15:00"]Output: false
Explanation: The two events do not intersect.
```

<strong>Constraints:</strong>

- `event1.length == event2.length == 2`
- `event1[i].length == event2[i].length == 5`
- `startTime1 <= endTime1`
- `startTime2 <= endTime2`
- All the event times follow the `HH:MM` format.

출처: LeetCode, https://leetcode.com/problems/determine-if-two-events-have-conflict
