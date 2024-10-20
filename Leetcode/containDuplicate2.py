class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hashDict = dict()
        for index in range(len(nums)):
            if nums[index] not in hashDict:
                hashDict[nums[index]] = index

            else:
                numIndex = hashDict[nums[index]]
                if (index - numIndex) <= k:
                    return True

                hashDict[nums[index]] = index

        return False


print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
