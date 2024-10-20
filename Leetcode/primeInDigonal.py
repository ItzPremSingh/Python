def isPrime(num: int) -> bool:
    if num < 2:
        return False

    if num == 2:
        return True

    for divisor in range(3, num // 2):
        if num % divisor == 0:
            return False

    return True


class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        numsLen = nums.__len__()
        diagonal1 = [nums[index][index] for index in range(numsLen)]
        diagonal2 = [nums[i][numsLen - i - 1] for i in range(numsLen)]
        diagonal3 = diagonal1 + diagonal2

        bigPrime = 0

        for num in diagonal3:
            if isPrime(num):
                if num > bigPrime:
                    bigPrime = num

        return bigPrime


print(Solution().diagonalPrime([[]]))
