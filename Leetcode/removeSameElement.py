class Solution:
    def removeDuplicates(self, nums: list[int]) -> tuple[int, list[int]]:
        lastElement = nums[0]
        numLen = len(nums)
        popElement = [lastElement]
        leftLen = numLen
        index = 1

        while index < numLen:
            element = nums[index]
            if element == lastElement:
                leftLen -= 1

            else:
                lastElement = element
                popElement.append(lastElement)

            index += 1

        return leftLen, popElement


print(Solution().removeDuplicates([1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5]))
