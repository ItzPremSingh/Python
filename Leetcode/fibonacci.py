class Solution:
    def fib(self, number: int) -> int:
        if number < 2:
            return number

        return self.fib(number - 1) + self.fib(number - 2)


print(Solution().fib(27))
