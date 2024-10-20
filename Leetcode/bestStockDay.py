class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = min(prices)
        minPriceDay = prices.index(minPrice)
        maxPrice = max(prices[minPriceDay:])

        return maxPrice - minPrice


print(Solution().maxProfit([7, 6, 4, 3, 1]))
