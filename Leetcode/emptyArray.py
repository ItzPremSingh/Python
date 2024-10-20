def isSmallest(_list: list[int]) -> bool:
    firstElement = _list[0]
    for number in _list[1:]:
        if firstElement > number:
            return False

    return True


class Solution:
    def countOperationsToEmptyArray(self, nums: list[int]) -> int:
        time = 0
        listLen = len(nums)
        start = 0

        while listLen != 0:
            if isSmallest(nums[start:]):
                start += 1
                listLen -= 1

            else:
                firstElement = nums[start]
                nums.append(firstElement)
                start += 1

            time += 1

        return time


_list = [1, 2, 3]
print(Solution().countOperationsToEmptyArray(_list))
