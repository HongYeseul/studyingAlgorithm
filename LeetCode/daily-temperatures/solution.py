class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)

        # 모든 날짜 돌면서 
        # for i in range(0, len(temperatures) -1):
        #     today = temperatures[i]
        #     # 자신의 온도보다 높을 때까지 +1
        #     j = i+1
        #     while j < len(temperatures)-1 and today >= temperatures[j]:
        #         j += 1
        #     # print(today, i, j)
        #     if today < temperatures[j]:
        #         result[i] = j - i
        #     elif j == len(temperatures)-1:
        #         result[i] = 0
        # if temperatures[len(temperatures)-2] >= temperatures[len(temperatures)-1]:
        #     result[len(temperatures) -2] = 0

        # 뒤에서부터 for문 돌리면서 누적합 계산
        for i in range(len(temperatures) -2, -1, -1):
            j = i +1

            while temperatures[j] <= temperatures[i]:
                if result[j] == 0:
                    break
                j += result[j]
            
            if temperatures[j] > temperatures[i]:
                result[i] = j - i
        
        return result
