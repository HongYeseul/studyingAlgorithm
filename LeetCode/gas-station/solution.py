class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        
        start = 0
        size = len(gas)

        def loop(start: int)-> (int, int):
            sum_ = 0
            for i in range(size):

                idx = (start + i) % size

                sum_ += ( gas[idx] - cost[idx] )
                if (sum_ < 0):
                    # print(start, idx, sum_)
                    return -1, i
                
            return start, start
        
        while start < size:
            n, m = loop(start)

            if (n >= 0):
                return n
            
            start += (m + 1)
        return -1
            
