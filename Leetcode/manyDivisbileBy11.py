class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        total = 0
        divisor = 11
        while divisor < n:
            print(divisor)
            total += 1
            divisor += 11

        return total


print(Solution().numDupDigitsAtMostN(100))
