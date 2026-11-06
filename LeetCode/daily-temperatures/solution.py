class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)

        # TODO 단조스택 문제로 분류됨. 
        # 정석으로 풀이하려면 ... 아직 더 따뜻한 날을 못 찾은 날짜의 인덱스를 스택에 저장해서 활용,,
        for i in range(len(temperatures) -2, -1, -1):
            j = i +1

            while temperatures[j] <= temperatures[i]:
                if result[j] == 0:
                    break
                j += result[j]
            
            if temperatures[j] > temperatures[i]:
                result[i] = j - i
        
        return result
