def reverse(number: int) -> int:
    reverseNum = 0

    while number > 0:
        digit = number % 10
        reverseNum = reverseNum * 10 + digit
        number //= 10

    return reverseNum


class Solution:
    def sumOfNumberAndReverse(self, number: int) -> bool:
        n = 1

        while n <= number:
            if n + reverse(n) == number:
                return True

            n += 1

        return False


print(Solution().sumOfNumberAndReverse(63))
