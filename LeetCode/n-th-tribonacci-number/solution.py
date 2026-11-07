class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            arr = [0, 1, 1]
            return arr[n]

        arr = [0] * (n+1)

        arr[0] = 0
        arr[1] = 1
        arr[2] = 1
        
        for i in range(3, n+1):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
        
        return arr[len(arr)-1]
