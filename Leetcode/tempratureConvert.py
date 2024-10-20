class Solution:
    def convertTemprature(self, celsius: float) -> list[float]:
        return [
            celsius + 273.15,
            celsius * 1.80 + 32.00,
        ]


print(Solution().convertTemprature(122.11))
