class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = [[] for _ in range(numRows)]
        row = 0
        direction = 1

        # 0 -> numRows까지는 +1
        # numRows -> 0까지는 -1
        for x in s:
            result[row].append(x)

            if row == 0:
                direction = 1
            elif row == numRows -1:
                direction = -1
            
            row += direction
        
        return "".join("".join(x) for x in result)
