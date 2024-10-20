class Solution:
    def breakInteger(self, integer: int) -> int:
        if integer == 2:
            return 1

        number = 1
        while number < integer:
            print(number)
            number += 1

        return 0


print(Solution().breakInteger(10))
