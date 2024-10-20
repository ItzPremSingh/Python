def sumOfSquare(n: int) -> int:
    _sum = 0

    while n > 0:
        digit = n % 10
        _sum += digit**2
        n //= 10

    return _sum


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = sumOfSquare(n)

        return n == 1


print(Solution().isHappy(19))
