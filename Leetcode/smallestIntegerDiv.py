class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1

        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length

        return -1


print(Solution().smallestRepunitDivByK(7))
