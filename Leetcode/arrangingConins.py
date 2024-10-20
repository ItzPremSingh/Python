class Solution:
    def arrangeCoins(self, n: int) -> int:
        totalRows = 0
        totalCoinToCompleteRow = 1

        while n >= totalCoinToCompleteRow:
            n -= totalCoinToCompleteRow
            totalCoinToCompleteRow += 1
            totalRows += 1

        return totalRows


print(Solution().arrangeCoins(9392))
