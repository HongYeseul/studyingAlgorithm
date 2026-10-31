class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        x = 0
        y = len(numbers) -1
        sum_ = numbers[x] + numbers[y]
        # while numbers[y] > target:
        #     y-=1

        while (sum_ != target and x != y):
            sum_ = numbers[x] + numbers[y]

            # target보다 sum이 작으면:
            if (target > sum_):
                x+=1
            
            # target보다 sum이 크면 
            if (target < sum_):
                y-=1
            # sum_ = numbers[x] + numbers[y]
            
            # print(x, y, sum_)
        
        if x == 0 and y == 0:
            return [1,2]

        return [x+1, y+1]

