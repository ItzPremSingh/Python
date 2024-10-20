class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        _sum = 0

        for num in nums:
            letSum = 0
            count = 2
            for div in range(2, (num // 2) + 1):
                if num % div == 0:
                    count += 1
                    letSum += div

            if count == 4:
                _sum += letSum + 1 + num

        return _sum


print(Solution().sumFourDivisors([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
