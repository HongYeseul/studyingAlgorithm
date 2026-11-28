class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        # event1이 even2보다 먼저 시작해야함
        event1_start_hour = int(event1[0].split(":")[0])
        event2_start_hour = int(event2[0].split(":")[0])

        if event1_start_hour > event2_start_hour:
            temp = event1
            event1 = event2
            event2 = temp
        
        event1_start_hour, event1_start_minute = map(int, event1[0].split(":"))
        event1_end_hour, event1_end_minute = map(int, event1[1].split(":"))
        event2_start_hour, event2_start_minute = map(int, event2[0].split(":"))
        event2_end_hour, event2_end_minute = map(int, event2[1].split(":"))

        result = False  

        # e1 끝나는 시간 < e2 시작 시간
        if event1_end_hour > event2_start_hour:
            result = True

        if event1_end_hour == event2_start_hour and event1_end_minute >= event2_start_minute:
            result = True

        # event2 끝나는 시간보다 event1 시작시간이 빠를 때 False
        if event1_start_hour == event2_end_hour and event1_start_minute >= event2_end_minute:
            result = False
        return result
