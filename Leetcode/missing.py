class Solution:
    def firstPositiveMissing(self, numbers: list[int]) -> int:
        numberSet = set(numbers)
        number = 1
        while True:
            if not number in numberSet:
                return number

            number += 1


print(Solution().firstPositiveMissing([7, 8, 9, 11, 12]))
