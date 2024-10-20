class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True

        strNum = str(num)

        if strNum[-1] == "0":
            return False

        return True

    def reverse(self, num: int) -> int:
        sign = False
        if num < 0:
            num = abs(num)
            sign = True

        reversed = 0
        while num != 0:
            remainder = num % 10
            reversed = reversed * 10 + remainder
            num = num // 10

        if sign:
            reversed = -reversed

        if reversed < -(2**31) or reversed > 2**31 - 1:
            return 0

        return reversed


print(Solution().reverse(1534236469))
