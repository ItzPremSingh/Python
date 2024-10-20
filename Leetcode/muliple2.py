class Solution:
    def smallestEvenMultiple(self, number: int) -> int:
        return number * 2 if number % 2 != 0 else number


print(Solution().smallestEvenMultiple(6))
