class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        differenceX = coordinates[1][0] - coordinates[0][0]
        differenceY = coordinates[1][1] - coordinates[0][1]

        lastX = coordinates[1][0]
        lastY = coordinates[1][1]

        index = 2

        while index < len(coordinates):
            x = coordinates[index][0]
            y = coordinates[index][1]

            if differenceX != x - lastX or differenceY != y - lastY:
                return False

            lastX, lastY = x, y
            index += 1

        return True


print(
    Solution().checkStraightLine(
        [
            [0, 0],
            [0, 1],
            [0, -1],
        ]
    )
)
