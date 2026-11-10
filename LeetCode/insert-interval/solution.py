class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        flag = False

        i  = 0
        while i < len(intervals):
            if not flag and newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                flag=True
                continue

            elif not flag and newInterval[0] <= intervals[i][1]:
                start = min(newInterval[0], intervals[i][0])
                idx = i
                # 구간 찾기
                while i < len(intervals) and newInterval[1] >= intervals[i][0]:
                    i+=1
                if (i != idx):
                    i-=1
                end = max(intervals[i][1], newInterval[1])
                result.append([start, end])
                flag = True
            
            else:
                result.append(intervals[i])
            i+=1
        
        if len(result) < 1:
            return [newInterval]
        if result[-1][1] < newInterval[0]:
            result.append(newInterval)
        return result
