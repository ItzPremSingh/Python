class Solution:
    def rotateSlow(self, array: list[int], times: int) -> None:
        for _ in range(times):
            last = array.pop()
            array.insert(0, last)

    def rotate(self, array: list[int], times: int) -> None:
        def _rotate(array: list[int]) -> None:
            lastElement = array[-1]
            index = 0
            arrayLen = len(array)

            while index < arrayLen:
                element = array[index]
                array[index] = lastElement
                lastElement = element
                index += 1

        for _ in range(times):
            _rotate(array)


_list = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(_list, 3)

print(_list)
