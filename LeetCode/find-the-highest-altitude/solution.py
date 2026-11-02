class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        result: list[int] = [0] * len(gain)

        result[0] = gain[0]
        highest = max(0, gain[0])
        for i in range(1, len(gain)):
            result[i] = result[i-1] + gain[i]

            if highest < result[i]:
                highest =  result[i]
        
        print(result)
        return highest
