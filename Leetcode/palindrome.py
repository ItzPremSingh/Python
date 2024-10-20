class Solution:
    def palindrome(self, num: int) -> bool | object:
        number = num
        if num == 0:
            return True

        if num < 0 or num % 10 == 0:
            return False

        reversed = 0
        while num != 0:
            remainder = num % 10
            reversed = reversed * 10 + remainder
            num = num // 10

        print(number, reversed)

        if reversed != number:
            return False

        return True


print(Solution().palindrome(0))
