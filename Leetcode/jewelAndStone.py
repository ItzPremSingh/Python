class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = set(jewels)
        number = 0

        for stone in stones:
            if stone in jewel:
                number += 1

        return number


print(Solution().numJewelsInStones(jewels = "z", stones = "ZZ"))
