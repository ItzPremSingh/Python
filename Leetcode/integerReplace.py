class Solution:
    def integerReplacement(self, n: int) -> int:
        number = n
        timeTakenInPlus = 0
        timeTakenInMinus = 0

        while n != 1:
            if n % 2 == 0:
                n //= 2

            else:
                n += 1

            timeTakenInPlus += 1

        n = number

        while n != 1:
            if n % 2 == 0:
                n //= 2

            else:
                n -= 1

            timeTakenInMinus += 1

        if timeTakenInPlus < timeTakenInMinus:
            return timeTakenInPlus

        return timeTakenInMinus


print(Solution().integerReplacement(10000))
