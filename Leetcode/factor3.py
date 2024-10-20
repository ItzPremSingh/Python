class Solution:
    def factorThree(self, number: int) -> bool:
        factorCount = 2
        aFactor = 2

        while aFactor <= number // 2:
            if number % aFactor == 0:
                factorCount += 1

            if factorCount > 3:
                return False

            aFactor += 1

        if factorCount == 3:
            return True

        return False


print(Solution().factorThree(4))
