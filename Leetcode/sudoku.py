class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def is_valid_row(row):
            seen = set()
            for num in row:
                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)
            return True

        def is_valid_column(board, col):
            seen = set()
            for row in board:
                num = row[col]
                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)
            return True

        def is_valid_box(board, start_row, start_col):
            seen = set()
            for i in range(3):
                for j in range(3):
                    num = board[start_row + i][start_col + j]
                    if num != ".":
                        if num in seen:
                            return False
                        seen.add(num)
            return True

        for i in range(9):
            if not is_valid_row(board[i]) or not is_valid_column(board, i):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not is_valid_box(board, i, j):
                    return False

        return True


board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]

print(Solution().isValidSudoku(board))
