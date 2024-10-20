class Solution:
    def fizBuzz(self, n: int) -> list[str]:
        result = []
        for num in range(1, n + 1):
            if num % 3 == num % 5 == 0:
                result.append("FizzBuzz")

            elif num % 3 == 0:
                result.append("Fizz")

            elif num % 5 == 0:
                result.append("Buzz")

            else:
                result.append(str(num))

        return result


print(Solution().fizBuzz(10**4))
