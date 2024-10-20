class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: list[int], indexDiff: int, valueDiff: int
    ) -> bool:
        hashDict = dict()
        for index in range(len(nums)):
            value = nums[index]
            if value not in hashDict:
                hashDict[value] = index

            else:
                if (
                    index - hashDict[value] <= indexDiff
                    and nums[hashDict[value]] - value <= valueDiff
                ):
                    return True

                hashDict[value] = index

        return False


print(Solution().containsNearbyAlmostDuplicate([8, 7, 15, 1, 6, 1, 9, 15], 1, 3))
