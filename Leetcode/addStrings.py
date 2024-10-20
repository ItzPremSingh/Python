def atoi(num: str) -> int:
    intNum = 0
    for digit in num:
        intNum = intNum * 10 + (ord(digit) - ord("0"))

    return intNum


class Solution:
    def addStrings(self, num1: str, num2: str) -> int:
        return atoi(num1) + atoi(num2)


print(Solution().addStrings("12", "363"))
