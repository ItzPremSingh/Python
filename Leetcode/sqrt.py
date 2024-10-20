class Solution:
    def mySqrt(self, number: int) -> int:
        guess = number / 2.0
        while abs(guess * guess - number) > 1e-6:
            guess = (guess + number / guess) / 2.0

        return int(guess)


print(Solution().mySqrt(8))
