class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        index = 1
        num = arr[0]
        isIncreasing = 1

        _len = arr.__len__()
        while index < _len:
            if isIncreasing:
                if num > arr[index]:
                    isIncreasing = 0

                elif num == arr[index]:
                    return False

            else:
                if num <= arr[index]:
                    return False

            num = arr[index]
            index += 1

        return True


print(Solution().validMountainArray([0, 3, 2, 1]))
