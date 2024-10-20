class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        numLen = len(nums)
        total = 0

        for i in range(numLen):
            for j in range(numLen):
                for k in range(numLen):
                    if (
                        i < j < k
                        and nums[j] - nums[i] == diff
                        and nums[k] - nums[j] == diff
                    ):
                        total += 1

        return total


print(Solution().arithmeticTriplets(nums=[4, 5, 6, 7, 8, 9], diff=2))
