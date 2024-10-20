class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashMap = set()
        for num in nums:
            if num not in hashMap:
                hashMap.add(num)
            else:
                return True

        return False


print(Solution().containsDuplicate([1, 3, 4, 2]))
