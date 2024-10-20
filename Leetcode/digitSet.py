class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        digitLen = len(digits)
        totalDigit = digitLen
        i, j = 0, 0

        while j < digitLen:
            if i == digitLen:
                i = 0
                j += 1

            number = int(digits[i] + digits[j])
            if number <= n:
                totalDigit += 1

            else:
                return digitLen

            i += 1

        return 0


print(Solution().atMostNGivenDigitSet(["1", "3", "5", "7"], 100))
