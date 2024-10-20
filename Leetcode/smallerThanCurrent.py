class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        return [sorted(nums).index(i) for i in nums]


print(Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
