class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        arr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []

        digit = list(map(int, list(digits)))
        print(digit)

        def dfs(index, current):
            # return
            if len(current) == len(digit):
                result.append(current)
                return

            for x in arr[digit[index]]:
                dfs(index+1, current + x)


        dfs(0, "")
        return result
