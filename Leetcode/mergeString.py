class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        small = word1
        big = word2
        start = 0
        _len = len(word1)

        if len(word2) > _len:
            small = word2
            big = word1
            _len = len(word2)
            start = 1

        small = list(small)
        big = list(big)
        count = 0

        while count < _len:
            big.insert(start, small[count])

            count += 1
            start += 2

        return "".join(big)


print(Solution().mergeAlternately("ace", "bdf"))
