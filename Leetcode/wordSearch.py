class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        letterToMatch = word[0]
        while True:
            for row in board:
                for element in row:
                    if element == letterToMatch:
                        pass
        return True


_list = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
]
print(Solution().exist(_list, "ABCCED"))
