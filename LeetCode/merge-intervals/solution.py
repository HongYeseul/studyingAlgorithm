class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        answer = [intervals[0]]

        for i in range(1, len(intervals)):
            if ( answer[len(answer)-1][1] >= intervals[i][0] and answer[len(answer)-1][1] <= intervals[i][1]):
                # answer의 마지막 end 값이랑 비교
                answer[len(answer)-1][1] = intervals[i][1]
            elif (answer[len(answer)-1][0] <= intervals[i][0] and answer[len(answer)-1][1] >= intervals[i][1]):
                continue
            else:
                answer.append(intervals[i])

        return (answer)
        
